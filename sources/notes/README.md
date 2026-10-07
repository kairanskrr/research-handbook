# 证据摘录

整理内容里的每条结论，都通过脚注指向这里的一条证据。证据记录资料原文在哪里、怎么说，让读者不用找全文也能核对。

只为整理内容实际引用到的资料写摘录，不需要一次把资料摘完。

## 文件

每份资料一个文件，文件名是它在 [`references.bib`](../../papers/references.bib) 中的 key，例如 `kitchenham2007guidelines.md`。推文串等没有 BibTeX 的资料，先在 `references.bib` 中补一条 `@misc`。

## 格式

```markdown
# Kitchenham & Charters 2007：Guidelines for performing Systematic Literature Reviews in Software Engineering

- 资料：`kitchenham2007guidelines`，[原文](https://legacyfileshare.elsevier.com/promis_misc/525444systematicreviewsguide.pdf)
- 版本：技术报告 v2.3

### E1

- 位置：§5.3，第 13 页
- 原文："..."
- 要点：（中文，一两句话说明这条证据支持什么）
```

规则：

- **原文**只引一两句，保留原语言，不要整段复制。引文中的参考文献编号（如 `[3]`）可以省略；中间省略的部分用 `[...]` 表示。
- **位置**写到章节或页码；网页写小标题。
- 编号 E1、E2……按添加顺序递增，被引用后不再改动。某条作废时保留编号，注明"已作废"及原因。

## 在整理内容中引用

用 Markdown 脚注，脚注里写资料简称、位置和证据链接：

```markdown
系统综述必须在开始检索前写好研究方案。[^kitchenham2007guidelines-e1]

[^kitchenham2007guidelines-e1]: Kitchenham & Charters 2007，§5.3。[证据](../../sources/notes/kitchenham2007guidelines.md#e1)
```
