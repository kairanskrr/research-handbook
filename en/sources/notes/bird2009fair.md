# Bird et al. 2009: Fair and Balanced? Bias in Bug-Fix Datasets

- Source: `bird2009fair`, [Original](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/bird2009fbb.pdf)
- Version: ESEC/FSE 2009 conference paper; author version on the Microsoft Research website.

### E1

- Location: Abstract
- Quote: "only a fraction of bug fixes are actually labelled in source code version histories, and thus become available for study in the extracted datasets." / "we investigate historical data from several software projects, and find strong evidence of systematic bias."
- Key point: Only a fraction of bug fixes are labelled in version histories and so end up in research datasets; across several projects the authors found strong evidence of systematic bias.

### E2

- Location: §1 Introduction
- Quote: "However, there is no standard or enforced practice to link a particular source code change to the corresponding entry in the bug database. Linkages, sadly, are irregular and inconsistent."
- Key point: There is no standard or enforced practice for linking a code change to its entry in the bug database, so the links are irregular and inconsistent.

### E3

- Location: §1 Introduction
- Quote: "Hypothesis-testing on this dataset might lead to the incorrect conclusion that more experienced developers make more mistakes"
- Key point: If experienced developers label their fixes more carefully, testing hypotheses on such data could lead to the false conclusion that more experienced developers make more mistakes.

### E4

- Location: §4 Data Gathering, Linking the Data Sources
- Quote: "Scan through the commit messages for numbers in a given format" / "Exclude all false-positive numbers (e.g., release numbers, year dates, etc.), which have a defined format." / "Check if the potential reference number exists in the bug database." / "Check if the referenced bug report has a fixing activity 7 days before or 7 days past the commit date."
- Key point: A common commit-to-bug linking method: scan commit messages for numbers in a given format, exclude false positives such as release numbers and years, check that the number exists in the bug database, and check that the bug shows fix activity within 7 days of the commit.

### E5

- Location: §4 Data Gathering, Linking the Data Sources
- Quote: "As additional verification, we manually inspected the results of our scan, looking for both false positives and false negatives."
- Key point: The authors manually inspected the results of their automatic linking, looking for both false positives (wrong links) and false negatives (missed links).
