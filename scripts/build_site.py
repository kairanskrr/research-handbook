"""Build the web reader of the handbook (GitHub Pages).

usage: python scripts/build_site.py --full <checkout> [--short <checkout>] --out <dir>

--full   a checkout of the full version (branch main)
--short  a checkout of the concise version (branch concise); optional
writes <out>/index.html and, for each language, <out>/<lang>/guide.json, notes.json and,
with --short, guide-short.json. Chinese comes from the checkout root, English from its en/ folder.
"""
import argparse, io, json, os, re, shutil

REWRITTEN = re.compile(r"^(README\.md|guide/faq\.md|guide/0[0-4]_.*|guide/08_.*)$")


LABELS = {
    "zh": {
        "sections": ["开始", "主线一 · 从兴趣到项目", "主线二 · 从项目到研究设计", "主线三 · 执行和分析", "主线四 · 写作和发表",
                     "研究套路", "研究方法", "学科篇", "贯穿全程"],
        "home": "首页", "fields": "学科篇总览", "subfields": "各方向总览", "practices": "实践总览", "overview": "总览：",
        "more": "其他", "faq": "常见问题速查", "sources": "资料列表", "contrib": "参与贡献",
    },
    "en": {
        "sections": ["Start here", "Part 1 · From interest to project", "Part 2 · From project to study design",
                     "Part 3 · Running the study and analyzing results", "Part 4 · Writing and publishing",
                     "Research strategies", "Research methods", "Fields", "Throughout the project"],
        "home": "Home", "fields": "All fields", "subfields": "Subfields overview", "practices": "Practices overview", "overview": "Overview: ",
        "more": "More", "faq": "FAQ: quick answers", "sources": "Source list", "contrib": "Contributing",
    },
}
DIRS = ["00_start-here", "01_from-interest-to-project", "02_from-project-to-study", "03_conduct-and-analyze",
        "04_write-and-publish", "05_research-strategies", "06_methods", "07_fields", "08_throughout"]


def bundle(REPO, lang="zh"):
    L = LABELS[lang]
    def rd(p):
        return io.open(os.path.join(REPO, p), encoding="utf8").read()


    def h1(text):
        m = re.search(r"^# (.+)$", text, re.M)
        return m.group(1).strip() if m else ""

    def short(title):
        return re.split(r"[：:]", title, 1)[0].strip()

    pages = {}
    def add(path):
        t = rd(path)
        pages[path] = {"title": h1(t), "md": t}

    SECTIONS = list(zip(DIRS, L["sections"]))

    def mdfiles(d):
        full = os.path.join(REPO, "guide", d)
        fs = sorted(f for f in os.listdir(full) if f.endswith(".md"))
        if "README.md" in fs:
            fs.remove("README.md"); fs.insert(0, "README.md")
        return ["guide/%s/%s" % (d, f) for f in fs]

    nav = []
    add("README.md")
    nav.append({"label": L["home"], "items": [{"path": "README.md", "label": "Research Handbook"}]})
    for d, label in SECTIONS:
        items = []
        if d == "07_fields":
            add("guide/07_fields/README.md")
            items.append({"path": "guide/07_fields/README.md", "label": L["fields"]})
            idx = rd("guide/07_fields/README.md")
            order = []
            for f in re.findall(r"\(([a-z-]+)/README\.md", idx):
                if f not in order:
                    order.append(f)
            if "computer-science" not in order:
                order.insert(1, "computer-science")
            for f in sorted(os.listdir(os.path.join(REPO, "guide/07_fields"))):
                if os.path.isdir(os.path.join(REPO, "guide/07_fields", f)) and f not in order:
                    order.append(f)
            for f in order:
                p = "guide/07_fields/%s/README.md" % f
                add(p)
                kids = []
                for sub, overview in (("subfields", L["subfields"]), ("practices", L["practices"])):
                    pd = os.path.join(REPO, "guide/07_fields", f, sub)
                    if not os.path.isdir(pd):
                        continue
                    group = []
                    for g in sorted(os.listdir(pd)):
                        if g.endswith(".md"):
                            q = "guide/07_fields/%s/%s/%s" % (f, sub, g)
                            add(q)
                            lab = overview if g == "README.md" else short(pages[q]["title"])
                            group.append({"path": q, "label": lab})
                    group.sort(key=lambda k: k["label"] != overview)
                    kids.extend(group)
                items.append({"path": p, "label": short(pages[p]["title"]), "children": kids})
        else:
            for p in mdfiles(d):
                add(p)
                lab = short(pages[p]["title"])
                if p.endswith("/README.md"):
                    lab = L["overview"] + lab if not lab.startswith(L["overview"].rstrip(": ：")) else lab
                items.append({"path": p, "label": lab})
        group = {"label": label, "items": items}
        if d[:2] in ("01", "02", "03", "04"):
            group["part"] = label.split("·", 1)[1].strip()
        nav.append(group)

    add("guide/faq.md")
    add("guide/README.md")
    add("sources/README.md")
    add("CONTRIBUTING.md")
    nav.append({"label": L["more"], "items": [
        {"path": "guide/faq.md", "label": L["faq"]},
        {"path": "sources/README.md", "label": L["sources"]},
        {"path": "CONTRIBUTING.md", "label": L["contrib"]},
    ]})

    notes = {}
    nd = os.path.join(REPO, "sources", "notes")
    for f in sorted(os.listdir(nd)):
        if f.endswith(".md"):
            notes[f[:-3]] = rd("sources/notes/" + f)
    if "README" in notes:
        pages["sources/notes/README.md"] = {"title": h1(notes["README"]), "md": notes.pop("README")}

    return {"nav": nav, "pages": pages}, notes


def dump(obj, path):
    with io.open(path, "w", encoding="utf8") as f:
        json.dump(obj, f, ensure_ascii=False, separators=(",", ":"))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", required=True)
    ap.add_argument("--short")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    for lang, sub in (("zh", ""), ("en", "en")):
        full = os.path.join(a.full, sub)
        if not os.path.isfile(os.path.join(full, "README.md")):
            print(lang, "missing, skipped")
            continue
        out = os.path.join(a.out, lang)
        os.makedirs(out, exist_ok=True)
        guide, notes = bundle(full, lang)
        dump(guide, os.path.join(out, "guide.json"))
        dump(notes, os.path.join(out, "notes.json"))
        short = os.path.join(a.short, sub) if a.short else None
        if short and os.path.isfile(os.path.join(short, "README.md")):
            sg, _ = bundle(short, lang)
            sv = {p: v["md"] for p, v in sg["pages"].items()
                  if REWRITTEN.match(p) and p in guide["pages"] and guide["pages"][p]["md"] != v["md"]}
            dump(sv, os.path.join(out, "guide-short.json"))
            print(lang, "concise pages", len(sv))
        print(lang, "pages", len(guide["pages"]), "notes", len(notes))
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copy(os.path.join(here, "..", "site", "index.html"), os.path.join(a.out, "index.html"))
    open(os.path.join(a.out, ".nojekyll"), "w").close()


if __name__ == "__main__":
    main()
