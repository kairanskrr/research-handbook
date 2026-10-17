"""Build the web reader of the handbook (GitHub Pages).

usage: python scripts/build_site.py --full <checkout> [--short <checkout>] --out <dir>

--full   a checkout of the full version (branch main)
--short  a checkout of the concise version (branch concise); optional
writes <out>/index.html and, for each language, <out>/<lang>/guide.json, notes.json and,
with --short, guide-short.json. Chinese comes from the checkout root, English from its en/ folder.
"""
import argparse, io, json, os, re, shutil

REWRITTEN = re.compile(r"^(README\.md|guide/faq\.md|guide/0[0-3]_.*|guide/08_.*)$")

# Navigation order: the two parts first, then reference, then writing (kept, not expanded this round)
SECTIONS = [("00_start-here", "start"), ("01_find-a-problem", "p1"), ("02_do-the-project", "p2"),
            ("06_methods", "types"), ("07_fields", "fields"), ("05_research-strategies", "why"),
            ("08_throughout", "throughout"), ("03_write-and-publish", "write")]
PARTS = ("p1", "p2")

LABELS = {
    "zh": {
        "start": "开始", "p1": "第一部分 · 想到一个好题目", "p2": "第二部分 · 把它做出来", "types": "研究类型",
        "fields": "学科规矩", "why": "为什么：研究套路", "throughout": "贯穿全程", "write": "写作和发表",
        "home": "首页", "fieldsall": "学科篇总览", "subfields": "各方向总览", "overview": "总览：", "infield": "（%s）",
        "more": "其他", "faq": "常见问题速查", "sources": "资料列表", "contrib": "参与贡献",
    },
    "en": {
        "start": "Start here", "p1": "Part 1 · Find a good problem", "p2": "Part 2 · Do the project", "types": "Research types",
        "fields": "Field conventions", "why": "Why: research strategies", "throughout": "Throughout the project",
        "write": "Writing and publishing",
        "home": "Home", "fieldsall": "All fields", "subfields": "Subfields overview", "overview": "Overview: ", "infield": " (%s)",
        "more": "More", "faq": "FAQ: quick answers", "sources": "Source list", "contrib": "Contributing",
    },
}


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

    def mdfiles(d):
        full = os.path.join(REPO, "guide", d)
        if not os.path.isdir(full):
            return []
        fs = sorted(f for f in os.listdir(full) if f.endswith(".md"))
        for first in ("why-this-handbook.md", "README.md"):
            if first in fs:
                fs.remove(first); fs.insert(0, first)
        return ["guide/%s/%s" % (d, f) for f in fs]

    def field_order():
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
        return order

    def plain(d):
        items = []
        for p in mdfiles(d):
            add(p)
            lab = short(pages[p]["title"])
            if p.endswith("/README.md"):
                lab = L["overview"] + lab if not lab.startswith(L["overview"].rstrip(": ：")) else lab
            items.append({"path": p, "label": lab})
        return items

    nav = []
    add("README.md")
    nav.append({"label": L["home"], "items": [{"path": "README.md", "label": "Research Handbook"}]})
    for d, key in SECTIONS:
        label = L[key]
        if d == "07_fields":
            add("guide/07_fields/README.md")
            items = [{"path": "guide/07_fields/README.md", "label": L["fieldsall"]}]
            for f in field_order():
                p = "guide/07_fields/%s/README.md" % f
                add(p)
                kids = []
                pd = os.path.join(REPO, "guide/07_fields", f, "subfields")
                if os.path.isdir(pd):
                    for g in sorted(os.listdir(pd)):
                        if g.endswith(".md"):
                            q = "guide/07_fields/%s/subfields/%s" % (f, g)
                            add(q)
                            kids.append({"path": q, "label": L["subfields"] if g == "README.md" else short(pages[q]["title"])})
                    kids.sort(key=lambda k: k["label"] != L["subfields"])
                items.append({"path": p, "label": short(pages[p]["title"]), "children": kids})
        elif d == "06_methods":
            # research types: cross-field methods plus the practices that only one field uses
            items = plain(d)
            extra = []
            for f in field_order():
                pd = os.path.join(REPO, "guide/07_fields", f, "practices")
                if not os.path.isdir(pd):
                    continue
                fp = "guide/07_fields/%s/README.md" % f
                if fp not in pages:
                    add(fp)
                fname = short(pages[fp]["title"])
                for g in sorted(os.listdir(pd)):
                    if g.endswith(".md") and g != "README.md":
                        q = "guide/07_fields/%s/practices/%s" % (f, g)
                        add(q)
                        extra.append({"path": q, "label": short(pages[q]["title"]) + L["infield"] % fname})
                rp = os.path.join(pd, "README.md")
                if os.path.isfile(rp):
                    add("guide/07_fields/%s/practices/README.md" % f)
            items += sorted(extra, key=lambda k: k["label"])
        else:
            items = plain(d)
        if not items:
            continue
        group = {"label": label, "items": items}
        if key in PARTS:
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
