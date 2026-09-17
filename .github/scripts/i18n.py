#!/usr/bin/env python3
"""calculator-free.com international SEO builder.

Rebuilds every page's hreflang cluster from what actually exists on disk,
and regenerates sitemap.xml with xhtml:link alternate annotations.

Idempotent. Never touches <ins class="adsbygoogle"> / push() pairs,
canonicals, GA4 or any other markup.
"""
import os, re, sys, datetime, xml.sax.saxutils as sx

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE = "https://calculator-free.com"

# Switcher / hreflang order. Keep in sync with LANG_META below.
LANGS = ["ar","zh","da","nl","fr","de","hi","id","it","ja","ko","no",
         "pl","pt","ru","es","sv","tr","vi"]
EN_REGIONS = ["en-GB","en-US","en-AU","en-CA","en-IE"]

# Dirs that are not languages / not deployable.
SKIP_DIRS = {".git","_stage","node_modules",".wrangler",".github","cdn-cgi","th"}
SKIP_FILES = {"404.html"}

ALT_RE = re.compile(r'^[ \t]*<link rel="alternate" hreflang="[^"]*" href="[^"]*">[ \t]*\r?\n', re.M)
CANON_RE = re.compile(r'(<link rel="canonical" href="[^"]*">)')


def inventory():
    """-> pages: list of (abspath, lang, key); clusters: key -> set(lang)"""
    pages, clusters = [], {}
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn != "index.html" or fn in SKIP_FILES:
                continue
            ap = os.path.join(dirpath, fn)
            rel = os.path.relpath(dirpath, ROOT).replace(os.sep, "/")
            rel = "" if rel == "." else rel
            parts = rel.split("/") if rel else []
            if parts and parts[0] in LANGS:
                lang, key = parts[0], "/".join(parts[1:])
            else:
                lang, key = "en", rel
            pages.append((ap, lang, key))
            clusters.setdefault(key, set()).add(lang)
    return pages, clusters


def url_for(lang, key):
    p = "" if lang == "en" else lang + "/"
    p += (key + "/") if key else ""
    return BASE + "/" + p


def alt_pairs(key, langs):
    """Ordered [(hreflang, url)] for one cluster. EN must exist."""
    out = []
    if "en" in langs:
        en = url_for("en", key)
        out.append(("x-default", en))
        out.append(("en", en))
        out += [(r, en) for r in EN_REGIONS]
    for l in LANGS:
        if l in langs:
            out.append((l, url_for(l, key)))
    return out


def write_hreflang(pages, clusters):
    changed = 0
    for ap, lang, key in pages:
        pairs = alt_pairs(key, clusters[key])
        block = "".join('<link rel="alternate" hreflang="%s" href="%s">\n' % p for p in pairs)
        with open(ap, encoding="utf-8") as f:
            html = f.read()
        new = ALT_RE.sub("", html)
        if not CANON_RE.search(new):
            print("  !! no canonical, skipped:", ap); continue
        new = CANON_RE.sub(lambda m: m.group(1) + "\n" + block.rstrip("\n"), new, count=1)
        if new != html:
            with open(ap, "w", encoding="utf-8", newline="") as f:
                f.write(new)
            changed += 1
    return changed


def load_existing_priorities(path):
    pri = {}
    if not os.path.exists(path):
        return pri
    txt = open(path, encoding="utf-8").read()
    for m in re.finditer(r"<loc>([^<]+)</loc>.*?<priority>([^<]+)</priority>", txt, re.S):
        pri[m.group(1)] = m.group(2)
    return pri


def default_priority(lang, key):
    if key == "":
        return "1.0" if lang == "en" else "0.9"
    if key in ("about","contact","privacy-policy","terms-of-use"):
        return "0.3"
    if key.startswith("blog"):
        return "0.6"
    if key.endswith("-calculators") or key == "bet-calculator":
        return "0.8"
    return "0.9" if lang == "en" else "0.8"


def write_sitemap(pages, clusters):
    sm = os.path.join(ROOT, "sitemap.xml")
    pri = load_existing_priorities(sm)
    rows = []
    for ap, lang, key in pages:
        loc = url_for(lang, key)
        lastmod = datetime.date.fromtimestamp(os.path.getmtime(ap)).isoformat()
        p = pri.get(loc, default_priority(lang, key))
        alts = "".join(
            '<xhtml:link rel="alternate" hreflang="%s" href="%s"/>' % (h, sx.escape(u))
            for h, u in alt_pairs(key, clusters[key]))
        rows.append((lang != "en", key, loc,
            "  <url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority>%s</url>"
            % (sx.escape(loc), lastmod, p, alts)))
    rows.sort(key=lambda r: (r[0], r[1] != "", r[1], r[2]))
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"'
           ' xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    out += [r[3] for r in rows]
    out.append("</urlset>")
    with open(sm, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(out) + "\n")
    return len(rows)


if __name__ == "__main__":
    pages, clusters = inventory()
    print("pages: %d   clusters: %d   languages: %d (+en)" % (len(pages), len(clusters), len(LANGS)))
    print("hreflang rewritten in %d files" % write_hreflang(pages, clusters))
    print("sitemap urls: %d" % write_sitemap(pages, clusters))
