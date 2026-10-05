# Merevo Resources：怎么做好科研

一套写给科研新手的中文文档：读完能明白怎么做好科研，并能照着完成实际的研究工作，包括持续几个月甚至更长的研究项目。内容来自资深研究者的经验和各领域公认的方法规范，每条结论都能追溯到原始资料。

> **现阶段**：先做通用篇和计算机领域篇，进度见[整理内容目录](guide/README.md)。

## 从哪里开始

| 想做什么 | 去哪里 |
|---|---|
| 学习怎么做科研 | [整理内容](guide/README.md)：通用篇 → 领域篇 → 研究类型 |
| 查某条结论的依据 | 点整理内容里的脚注，跳到 [证据摘录](sources/notes/README.md) |
| 找原始资料：论文、规范、博客、仓库 | [原始资料列表](sources/README.md) |

## 仓库结构

仓库分两部分：**整理内容**是我们写的文档；**原始资料**是收集来的一手资料。整理内容中的每条结论都用脚注指向原始资料中的证据。

```
guide/          整理内容（中文）
  general/        通用篇
  fields/         领域篇，按 OECD（经济合作与发展组织）的学科分类组织；每个领域下有 research-types/
sources/        原始资料
  README.md       资料列表（awesome 列表形式）
  notes/          证据摘录：资料原文在哪里、怎么说
papers/         论文的 BibTeX（references.bib）、索引和本地 PDF
repos/          GitHub 仓库，以 git submodule 方式引入
internal/       团队内部材料
templates/      文档模板
scripts/        论文下载脚本
```

克隆本仓库时请使用 `git clone --recursive`，或在克隆后运行 `git submodule update --init`。

## 贡献

见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。
