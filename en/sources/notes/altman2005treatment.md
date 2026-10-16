# Altman & Bland 2005: Treatment allocation by minimisation

- Source: `altman2005treatment`, [original](https://pmc.ncbi.nlm.nih.gov/articles/PMC556084/)
- Version: BMJ 2005;330(7495):843, "Statistics Notes" series (DOI 10.1136/bmj.330.7495.843). These excerpts come from the full text in PubMed Central at the US National Library of Medicine.

### E1

- Location: main text, paragraph 1
- Quote: "The only widely acceptable alternative approach is minimisation" / "a method of ensuring excellent balance between groups for several prognostic factors, even in small samples. With minimisation the treatment allocated to the next participant enrolled in the trial depends (wholly or partly) on the characteristics of those participants already enrolled. The aim is that each allocation should minimise the imbalance across multiple factors."
- Key point: Minimisation gives excellent balance between groups on several prognostic factors, even in small samples; the allocation of the next participant depends (wholly or partly) on the characteristics of those already enrolled, so that each allocation minimizes imbalance across several factors.

### E2

- Location: main text, paragraphs 3–4
- Quote: "The first participant is allocated a treatment at random. For each subsequent participant we determine which treatment would lead to better balance between the groups in the variables of interest." / "(Note that two or more categories need to be constructed for continuous variables.)"
- Key point: The first participant is allocated at random; for each subsequent participant, determine which group would give better balance on the variables of interest. Continuous variables must first be split into two or more categories.

### E3

- Location: main text, paragraphs 5–6
- Quote: "We formalise this by summing over the four variables the numbers of participants with the same characteristics as this new recruit already in the trial" / "Imbalance is minimised by allocating this person to the group with the smaller total (or at random if the totals are the same)."
- Key point: The algorithm: for each group, sum the numbers of already-enrolled participants who share the new recruit's characteristic on each factor; allocate the recruit to the group with the smaller total, and at random if the totals are equal.

### E4

- Location: main text, paragraph 7
- Quote: "We use weighted randomisation so that there is a high chance (eg 80%) of each participant getting the treatment that minimises the imbalance. The use of a random element will slightly worsen the overall imbalance between the groups, but balance will be much better for the chosen variables than with simple randomisation. A random element also makes the allocation more unpredictable, although minimisation is a secure allocation system when used by an independent person."
- Key point: A random element can be added: allocate with high probability (e.g., 80%, the paper's example) to the group that minimizes imbalance. Balance is slightly worse, but still much better than simple randomization, and allocation is harder to predict.
