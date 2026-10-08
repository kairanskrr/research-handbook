"""Build the web reader of the handbook (GitHub Pages).

usage: python scripts/build_site.py --full <checkout> [--short <checkout>] --out <dir>

--full   a checkout of the full version (branch main)
--short  a checkout of the concise version (branch concise); optional
writes <out>/index.html, guide.json, notes.json and, with --short, guide-short.json
"""
import argparse, io, json, os, re, shutil

REWRITTEN = re.compile(r"^(README\.md|guide/faq\.md|guide/0[0-4]_.*|guide/08_.*)$")


def bundle(REPO):
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

    SECTIONS = [
        ("00_start-here", "开始"),
        ("01_from-interest-to-project", "主线一 · 从兴趣到项目"),
        ("02_from-project-to-study", "主线二 · 从项目到研究设计"),
        ("03_conduct-and-analyze", "主线三 · 执行和分析"),
        ("04_write-and-publish", "主线四 · 写作和发表"),
        ("05_research-strategies", "研究套路"),
        ("06_methods", "研究方法"),
        ("07_fields", "学科篇"),
        ("08_throughout", "贯穿全程"),
    ]

    def mdfiles(d):
        full = os.path.join(REPO, "guide", d)
        fs = sorted(f for f in os.listdir(full) if f.endswith(".md"))
        if "README.md" in fs:
            fs.remove("README.md"); fs.insert(0, "README.md")
        return ["guide/%s/%s" % (d, f) for f in fs]

    nav = []
    add("README.md")
    nav.append({"label": "首页", "items": [{"path": "README.md", "label": "Research Handbook"}]})
    for d, label in SECTIONS:
        items = []
        if d == "07_fields":
            add("guide/07_fields/README.md")
            items.append({"path": "guide/07_fields/README.md", "label": "学科篇总览"})
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
                pd = os.path.join(REPO, "guide/07_fields", f, "practices")
                if os.path.isdir(pd):
                    for g in sorted(os.listdir(pd)):
                        if g.endswith(".md"):
                            q = "guide/07_fields/%s/practices/%s" % (f, g)
                            add(q)
                            lab = "实践总览" if g == "README.md" else short(pages[q]["title"])
                            kids.append({"path": q, "label": lab})
                    kids.sort(key=lambda k: k["label"] != "实践总览")
                items.append({"path": p, "label": short(pages[p]["title"]), "children": kids})
        else:
            for p in mdfiles(d):
                add(p)
                lab = short(pages[p]["title"])
                if p.endswith("/README.md"):
                    lab = "总览：" + lab if not lab.startswith("总览") else lab
                items.append({"path": p, "label": lab})
        nav.append({"label": label, "items": items})

    add("guide/faq.md")
    add("guide/README.md")
    add("sources/README.md")
    add("CONTRIBUTING.md")
    nav.append({"label": "其他", "items": [
        {"path": "guide/faq.md", "label": "常见问题速查"},
        {"path": "sources/README.md", "label": "资料列表"},
        {"path": "CONTRIBUTING.md", "label": "参与贡献"},
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
    os.makedirs(a.out, exist_ok=True)
    guide, notes = bundle(a.full)
    dump(guide, os.path.join(a.out, "guide.json"))
    dump(notes, os.path.join(a.out, "notes.json"))
    if a.short:
        sg, _ = bundle(a.short)
        short = {p: v["md"] for p, v in sg["pages"].items()
                 if REWRITTEN.match(p) and p in guide["pages"] and guide["pages"][p]["md"] != v["md"]}
        dump(short, os.path.join(a.out, "guide-short.json"))
        print("concise pages", len(short))
    here = os.path.dirname(os.path.abspath(__file__))
    shutil.copy(os.path.join(here, "..", "site", "index.html"), os.path.join(a.out, "index.html"))
    open(os.path.join(a.out, ".nojekyll"), "w").close()
    print("pages", len(guide["pages"]), "notes", len(notes))


if __name__ == "__main__":
    main()
