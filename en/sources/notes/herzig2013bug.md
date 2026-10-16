# Herzig, Just, and Zeller 2013: It's Not a Bug, It's a Feature: How Misclassification Impacts Bug Prediction

- Source: `herzig2013bug`, [Original](https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf)
- Version: ICSE 2013 conference paper, the version posted on the website of the authors' software engineering group at Saarland University; the original site is currently unreachable, so it was read via the Internet Archive copy `https://web.archive.org/web/2019id_/https://www.st.cs.uni-saarland.de/publications/files/herzig-icse-2013.pdf`.

### E1

- Location: Abstract
- Quote: "we found 33.8% of all bug reports to be misclassified—that is, rather than referring to a code fix, they resulted in a new feature, an update to documentation, or an internal refactoring." / "On average, 39% of files marked as defective actually never had a bug."
- Key point: A manual check of more than 7,000 issue reports from five open-source projects found that 33.8% of reports labeled "bug" were actually new features, documentation updates, or refactorings; on average, 39% of files marked as defective never had a bug.

### E2

- Location: §I Introduction
- Quote: "However, all this assumes that the category of the issue report is accurate."
- Key point: Pulling "bug" reports out with a database query looks simple, but it assumes the category of each report is accurate.

### E3

- Location: Fig. 1; §XI Threats to Validity
- Quote: "Second author classifies all reports marked as misclassified by first author (without knowing the new category)." / "we chose a setup that ensures that every misclassified bug report is cross-validated and that classification conflicts have to pass a third inspection."
- Key point: The manual classification process: the first author classified the reports, the second author re-checked them without knowing the first author's verdict, and conflicts went through a third inspection.

### E4

- Location: §XI Threats to Validity
- Quote: "There exists no clear definition-separating feature and improvement requests." / "We counter this threat by listing the complete rules verbatim."
- Key point: The boundaries between categories are themselves unclear, and a different set of classification rules would change the results; the authors respond by listing their complete rules verbatim.

### E5

- Location: §XII Conclusion and Consequences
- Quote: "automated quantitative analysis should always include human qualitative analysis of the input data—and of the findings. Approaches relying on bug datasets should be preceded by a careful manual validation of data quality; at least of a significant sample. Data quality should be discussed as a threat to validity."
- Key point: Automated quantitative analysis should always include human qualitative analysis of the input data and of the findings; before using a bug dataset, manually validate a large enough sample and discuss data quality as a threat to validity.
