# 贡献规则

## 基本原则

1. **每条内容都要注明出处**。没有出处的内容不要写。属于本项目自己的分析、不来自文献的内容，标注"本项目分析"。
2. **不复制受版权保护的全文或 PDF**。用自己的话概括，必要时可以简短引用并注明出处。PDF 只保存在本地的 `papers/pdf/`（已加入 `.gitignore`），只有开放许可的论文才可以提交。
3. **不确定就标"待确认"**，不要猜测。
4. 用中文撰写；资料标题、术语和文件名保留英文。

## 添加一篇论文

1. 核实标题、作者、出处和 DOI（打开原始页面确认）。
2. 在 `papers/references.bib` 中添加条目。无法核实的 DOI 不要写，在 `note` 中说明。
3. 在 `papers/README.md` 的表格中添加一行，注明免费全文的来源；付费的放进"待获取"。
4. 如果有合法的免费全文，在 `scripts/fetch_papers.sh` 中添加下载地址。
5. 在 `README.md` 的对应分类下添加条目，格式为：

   ```
   - [标题](链接) - 作者，出处 年份。一句话说明用途。🆓 `bibtex-key`
   ```

## 添加一个 GitHub 仓库

1. 确认仓库确实存在、有实际内容，并记下许可证。
2. 在 `repos/README.md` 中记录上游地址、固定版本（当前默认分支的完整 commit hash）、提交日期和许可。
3. 在 `README.md` 的对应分类下添加条目，注明许可和更新情况（例如长期未更新）。

## 整理一类研究

使用 [`templates/research-type.md`](templates/research-type.md) 模板，结果放在 `research-types/` 下，并在 `README.md` 的"本仓库的整理笔记"表格中更新状态。

## 许可说明

- ACM SIGSOFT Empirical Standards 采用 CC0 1.0，可以自由引用和改编，但仍需注明出处。
- 其他资料各有版权或许可，见 `repos/README.md` 和 `papers/README.md`。
- 本仓库应保持私有，因为 `internal/` 会存放团队的审稿意见和决策记录。
