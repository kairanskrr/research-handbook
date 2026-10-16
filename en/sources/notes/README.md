# Evidence notes

Every conclusion in the curated content points, through a footnote, to an evidence entry here. An entry records where the original source says something and what exactly it says, so readers can check it without finding the full text.

Write notes only for sources the curated content actually cites. There is no need to excerpt a whole source at once.

## Files

One file per source, named after its key in [`references.bib`](../../../papers/references.bib), for example `kitchenham2007guidelines.md`. For sources with no BibTeX entry, such as tweet threads, first add an `@misc` entry to `references.bib`.

## Format

```markdown
# Kitchenham & Charters 2007: Guidelines for performing Systematic Literature Reviews in Software Engineering

- Source: `kitchenham2007guidelines`, [original](https://legacyfileshare.elsevier.com/promis_misc/525444systematicreviewsguide.pdf)
- Version: Technical report v2.3

### E1

- Location: §5.3, p. 13
- Quote: "..."
- Key point: (one or two sentences on what this evidence supports)
```

Rules:

- **Quote**: quote only one or two sentences, in the original language; don't copy whole paragraphs. Reference numbers inside the quote (such as `[3]`) can be dropped; mark omitted parts with `[...]`.
- **Location**: give the section or page; for web pages, give the subheading.
- Numbers E1, E2, … increase in the order entries are added and never change once cited. If an entry becomes invalid, keep its number and mark it "withdrawn" with the reason.

## Citing in the curated content

Use Markdown footnotes. In the footnote, give the short name of the source, the location, and a link to the evidence:

```markdown
A systematic review must have a written protocol before the search begins.[^kitchenham2007guidelines-e1]

[^kitchenham2007guidelines-e1]: Kitchenham & Charters 2007, §5.3. [Evidence](kitchenham2007guidelines.md#e1)
```
