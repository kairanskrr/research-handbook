# Contributing

## The two parts of the repository

- **Original sources**: `sources/` (the source list and evidence notes), `papers/`, `repos/`. These are only registered and excerpted, never reworked.
- **Curated content**: `guide/`, the handbook we write for people new to research. Every fact must be backed by evidence in the original sources.

## Basic principles

1. **Every piece of content must cite its source.** Don't write a fact you can't source. This project's own analysis and advice carries no footnote and no extra marker (see "How to write" below).
2. **Don't copy copyrighted full texts or PDFs.** Summarize in your own words; quote briefly where necessary and cite the source. PDFs are kept only locally in `papers/pdf/` (already in `.gitignore`); only openly licensed papers may be committed.
3. **If you're not sure, mark it "To be confirmed".** Don't guess.
4. Write the Chinese source edition in Chinese; keep source titles, technical terms, and file names in English. The English edition lives in `en/` and mirrors the Chinese edition page for page.

## Adding a paper

1. Verify the title, authors, venue, and DOI (open the original page to confirm).
2. Add an entry to `papers/references.bib`. Don't include a DOI you can't verify; explain in the `note` field instead.
3. Add a row to the table in `papers/README.md`, noting where a free full text can be found; put paywalled papers under "To obtain".
4. If there is a legal free full text, add its download URL to `scripts/fetch_papers.sh`.
5. Add an entry under the matching category in `sources/README.md`, in this format:

   ```
   - [Title](https://link-to-the-original) - Authors, Venue Year. One sentence on what it is used for. 🆓 `bibtex-key`
   ```

## Adding a GitHub repository

1. Confirm the repository really exists, has real content, and note its license.
2. In `repos/README.md`, record the upstream URL, the pinned version (the full commit hash of the current default branch), the commit date, and the license.
3. Add an entry under the matching category in `sources/README.md`, noting the license and how actively it is maintained (for example, not updated for a long time).

## Writing curated content

### Where new content goes

For how the handbook is meant to be read, see [`guide/00_start-here/how-to-use.md`](guide/00_start-here/how-to-use.md). In short:

| Content | Where it goes |
|---|---|
| What you need to think through and produce while finding a problem (entering a field, finding problems, exploring, screening, converging) | Part 1 · Find a good problem: `guide/01_find-a-problem/`, following the chapter template (plan §6) |
| What you need to think through and produce while doing the project (evidence, method, plan, validity, trial runs, running, analysis, decision points) | Part 2 · Do the project: `guide/02_do-the-project/`, following the chapter template |
| What knowledge a kind of research produces, what evidence it needs, which methods it commonly uses, which fields use it | Why (research strategies): `guide/05_research-strategies/` |
| How to do a specific kind of research well, when two or more fields use it | A shared method under Research types: `guide/06_methods/`, plus a new row in the lookup tables in `guide/06_methods/README.md` |
| A research practice used in only one field | That field's `practices/` (e.g. `guide/07_fields/computer-science/practices/`); the navigation groups it with the shared methods under Research types, so also add a row to the lookup tables in `guide/06_methods/README.md` |
| Conventions specific to a field or a community | Fields: `guide/07_fields/<field>/README.md`. Write only what is specific to the field; link general methods to `guide/06_methods/` |
| Things you face throughout, not at one stage (planning, materials, collaboration, integrity, mindset) | Throughout the project: `guide/08_throughout/` |

Pages on research methods and field-specific practices can use the [`templates/research-type.md`](../templates/research-type.md) template.

### How to write

1. **Write plainly.** Use Chinese, short sentences, and the second person; start from the reader's confusion at that moment; give the how-to first, then the why. Keep terms consistent with [`guide/00_start-here/key-concepts.md`](guide/00_start-here/key-concepts.md), and spell out abbreviations on first use.
2. **Footnote facts sentence by sentence.** An author's advice, a study's finding, a standard's requirement, a number: each sentence gets a footnote pointing to an evidence entry in `sources/notes/<key>.md`, and the original quote in that entry must actually support the sentence. For a source with no notes yet, add them first following the format in [`sources/notes/README.md`](sources/notes/README.md).
3. **Write advice we synthesized as plain text, with no footnote and no marker.** Practice tables, decision rules, examples, and other content that no single source states word for word are recognizable as ours because they have no footnote; facts embedded in the same paragraph still get their own footnotes. Two cases need saying in words: when our inference follows right after a cited source and a reader might take it for the source's view, write "so…", "we suggest…" or similar; when we judge a source itself (e.g. "the paper has no threats-to-validity section"), say that this is our judgment after reading the whole text.
4. **Mark anything uncertain `[To be confirmed]`**; where you can't find a reliable basis, write "Our sources do not cover this" rather than writing from memory.
5. **Write "Where sources disagree" only when the disagreement affects what you do**: set out each side's approach and reasons side by side, then give the handbook's own practical recommendation. Don't force them into a single conclusion.
6. **Say which field a source comes from.** Don't present practices from computer science, software engineering, or machine learning as rules for every field.

### Update the contents pages when you're done

When you add or change a chapter, method, or field page, update the contents page it belongs to as well: for chapters in the two Parts, the contents in the repository home page [`README.md`](../README.md); for research strategies, [`guide/05_research-strategies/README.md`](guide/05_research-strategies/README.md); for research types (shared methods and field-specific practices), [`guide/06_methods/README.md`](guide/06_methods/README.md); for Fields and each field's specific practices, also update [`guide/07_fields/README.md`](guide/07_fields/README.md); for Throughout the project, [`guide/08_throughout/README.md`](guide/08_throughout/README.md).

## Licensing notes

- The ACM SIGSOFT Empirical Standards (from the Association for Computing Machinery's Special Interest Group on Software Engineering) are released under CC0 1.0. They can be freely quoted and adapted, but you should still cite them.
- Other sources each have their own copyright or license; see `repos/README.md` and `papers/README.md`.
