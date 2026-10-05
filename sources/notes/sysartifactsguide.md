# sysartifacts：系统领域会议的制品评估指南

- 资料：`sysartifactsguide`，[原文](https://sysartifacts.github.io/)
- 版本：submodule `repos/sysartifacts__sysartifacts.github.io`，commit `26f4436`（2026-09-19）。引用了 `packaging-guide.md`（作者打包指南）和 `_conferences/osdi2024/artifacts-call.md`（OSDI '24 制品征集）。仓库未见许可证文件，只作简短引用。

### E1

- 位置：OSDI '24 Call for Artifacts，Benefits and Goals
- 原文："For now, artifact evaluation will begin only after paper acceptance decisions have already been made. Artifact evaluation is optional, although we hope all papers will participate."
- 要点：制品评估在论文录用之后才开始，自愿参加。

### E2

- 位置：OSDI '24 Call for Artifacts，Overview
- 原文："Because the time between paper acceptance and artifact submission is short, we strongly encourage authors to start preparing their artifacts for evaluation while their papers are still under consideration by the OSDI Program Committee."
- 要点：录用到提交制品之间时间很短，论文还在审时就该开始准备制品。

### E3

- 位置：OSDI '24 Call for Artifacts，Overview
- 原文："Last year, [...]64% of accepted OSDI papers[...] participated in the artifact evaluation process."
- 要点：OSDI 2023 有 64% 的录用论文参加了制品评估。

### E4

- 位置：OSDI '24 Call for Artifacts，Criteria
- 原文："Thus, the AEC's decision will be that the artifacts do or do not "conform to the expectations set by the paper.""
- 要点：评估标准是制品是否符合论文本身设定的预期。

### E5

- 位置：Packaging guide，Tools and tips
- 原文："Try out your own artifact on a blank environment"
- 要点：按自己写的步骤，在一个全新的环境里把制品跑一遍。

### E6

- 位置：Packaging guide，Formats
- 原文："This is the preferred method for artifacts with nontrivial dependencies."
- 要点：依赖复杂的制品，首选容器或虚拟机打包。

### E7

- 位置：Packaging guide，Formats
- 原文："Any such artifact must be boldly and explicitly flagged, both at submission time and in the artifact's instructions, so that evaluators and researchers can take appropriate precautions before installing and running these artifacts."
- 要点：安全研究等带有恶意或破坏性操作的制品，必须醒目标明，让评估者提前做好防护。
