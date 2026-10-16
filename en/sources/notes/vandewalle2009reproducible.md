# Vandewalle, Kovačević & Vetterli 2009: Reproducible Research in Signal Processing — What, why, and how

- Source: `vandewalle2009reproducible`, [original](https://infoscience.epfl.ch/record/136640)
- Version: IEEE Signal Processing Magazine 26(3), May 2009, pp. 37-47. Read from the full-text PDF publicly available on Infoscience, the institutional repository of the Swiss Federal Institute of Technology in Lausanne (EPFL), downloaded 2026-10-06. Locations give the subheading and journal page number.

### E1

- Location: Opening, p. 37
- Quote: "For a computational algorithm, details such as the exact data set, initialization or termination procedures, and precise parameter values are often omitted in the publication for various reasons, such as a lack of space, a lack of self-discipline, or an apparent lack of interest to the readers, to name a few."
- Key point: The authors observe that algorithm papers often omit the exact data set, initialization and termination procedures, and precise parameter values, for reasons such as lack of space, lack of self-discipline, or assuming readers don't care.

### E2

- Location: When is research reproducible, and when is it not?, p. 39
- Quote: "A research work is called reproducible if all information relevant to the work, including, but not limited to, text, data and code, is made available, such that an independent researcher can reproduce the results."
- Key point: The paper's definition of "reproducible research": all information relevant to the work (including text, data, and code) is made available so that an independent researcher can reproduce the results.

### E3

- Location: Reproducible research study, p. 40
- Quote: "We performed a study on all of the 134 papers published in IEEE Transactions on Image Processing in 2004." / "Finally, code (9%) and data (33%) are only available online in a minority of the cases"
- Key point: The authors checked all 134 papers in IEEE Transactions on Image Processing from 2004: only 9% made code available and 33% made data available.

### E4

- Location: Failures of reproducibility, p. 41
- Quote: "As different versions of this image circulate on the Web, it is often difficult to know on which version the simulations were performed."
- Key point: Common test images (such as Lena) circulate online in several versions, and readers often cannot tell which version a paper used, which hampers reproduction.

### E5

- Location: Failures of reproducibility, p. 41
- Quote: "Even we as authors are not able to reproduce the results, as we have different versions of the code on our disk, and it is unclear with which version the images in the final version were created."
- Key point: The authors admit they could not reproduce one of their own earlier papers: there were several versions of the code on their disk, and it was unclear which one produced the figures in the final version.

### E6

- Location: How to do reproducible research? — Experiments, pp. 41–42
- Quote: "Practical experiments are, by their nature, probably the most difficult type of work to reproduce." / "Often, it is not even feasible to repeat the exact experiments, as results can in the best case only be statistically equivalent to the original results. Therefore, in this case, we opt for reusability rather than reproducibility of the data."
- Key point: Physical experiments are the hardest to reproduce, often at best giving statistically equivalent results; the fallback is to make the measurement data reusable by others.

### E7

- Location: How to do reproducible research? — Experiments, p. 42
- Quote: "Next to the measurement data, a detailed description of the experimental setup and measurement devices should still be given, for those interested in understanding the exact setup or in performing similar experiments."
- Key point: Besides the measurement data, give a detailed description of the experimental setup and measurement devices.

### E8

- Location: How to do reproducible research? — Algorithms, p. 41
- Quote: "While in theory, the code is supposed to be platform or hardware independent, it is useful to specify the platform on which the tests were performed."
- Key point: Even if code is in theory platform- and hardware-independent, state the platform and software versions used for testing.

### E9

- Location: Implementation and issues, p. 43
- Quote: "Often, in a company, the work is only published after it has been protected by a patent." / "Still, many companies funding university research or doing research themselves consider the know-how attached to a patent valuable and are not willing to have the resulting code distributed online."
- Key point: Companies often publish only after filing a patent, and companies funding university research may also be reluctant to release code.

### E10

- Location: Implementation and issues, p. 43
- Quote: "Note also that, even if the code and data are not made available online, it may be very useful to set reproducible research standards internally, such that colleagues inside the company can reproduce the results."
- Key point: When code and data cannot be made public, at least set internal reproducibility standards so colleagues inside the organization can reproduce the results.

### E11

- Location: Case study: super-resolution, p. 42
- Quote: "It took about one week to check all the results and make sure they were reproducible, clean up and document the MATLAB code, and put everything online." / "done in about one day. We already had reproducibility in mind from the start"
- Key point: The first time, preparing reproducible materials after the fact took the authors about a week; later, with reproducibility in mind from the start, the same work took about a day.

### E12

- Location: How to do reproducible research? — Components, p. 41
- Quote: "signal processing can be considered as a hybrid between theoretical and experimental sciences." / "Often, to develop an intuitive feel for the results, a theorem is complemented by numerical simulations."
- Key point: The authors see signal processing as a hybrid of theoretical and experimental science; research has theoretical, algorithmic, and experimental parts, each with different reproducibility requirements, and theorems are often complemented by numerical simulations to build intuition.

### E13

- Location: Case study: super-resolution, p. 42
- Quote: "For each figure or table in the papers, there is a MATLAB script figure_x.m or table_y.m that reproduces the figure or table."
- Key point: The authors wrote one script for every figure and table in their papers; running it regenerates that figure or table.
