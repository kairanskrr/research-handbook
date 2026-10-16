# sysartifacts: artifact evaluation guide for systems conferences

- Source: `sysartifactsguide`, [original](https://sysartifacts.github.io/)
- Version: submodule `repos/sysartifacts__sysartifacts.github.io`, commit `26f4436` (2026-09-19). Cites `packaging-guide.md` (the packaging guide for authors) and `_conferences/osdi2024/artifacts-call.md` (the OSDI '24 call for artifacts). No license file was found in the repository, so only short quotations are used.

### E1

- Location: OSDI '24 Call for Artifacts, Benefits and Goals
- Quote: "For now, artifact evaluation will begin only after paper acceptance decisions have already been made. Artifact evaluation is optional, although we hope all papers will participate."
- Key point: Artifact evaluation starts only after a paper is accepted, and participation is voluntary.

### E2

- Location: OSDI '24 Call for Artifacts, Overview
- Quote: "Because the time between paper acceptance and artifact submission is short, we strongly encourage authors to start preparing their artifacts for evaluation while their papers are still under consideration by the OSDI Program Committee."
- Key point: The time between acceptance and artifact submission is short, so start preparing the artifact while the paper is still under review.

### E3

- Location: OSDI '24 Call for Artifacts, Overview
- Quote: "Last year, [...]64% of accepted OSDI papers[...] participated in the artifact evaluation process."
- Key point: At OSDI 2023, 64% of accepted papers took part in artifact evaluation.

### E4

- Location: OSDI '24 Call for Artifacts, Criteria
- Quote: "Thus, the AEC's decision will be that the artifacts do or do not "conform to the expectations set by the paper.""
- Key point: The evaluation criterion is whether the artifact meets the expectations set by the paper itself.

### E5

- Location: Packaging guide, Tools and tips
- Quote: "Try out your own artifact on a blank environment"
- Key point: Run through the artifact in a completely fresh environment, following your own instructions.

### E6

- Location: Packaging guide, Formats
- Quote: "This is the preferred method for artifacts with nontrivial dependencies."
- Key point: For artifacts with complex dependencies, packaging in a container or virtual machine is preferred.

### E7

- Location: Packaging guide, Formats
- Quote: "Any such artifact must be boldly and explicitly flagged, both at submission time and in the artifact's instructions, so that evaluators and researchers can take appropriate precautions before installing and running these artifacts."
- Key point: Artifacts that perform malicious or destructive operations, such as in security research, must be clearly flagged so that evaluators can take precautions in advance.
