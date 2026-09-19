#!/usr/bin/env python3
"""No calculator input was programmatically labelled: the <label> sat next to
the <input> with no for/id link and no aria-label, so a screen reader announced
"edit text, blank" for every field (WCAG 1.3.1 / 4.1.2).

Link each label to the field that follows it. Radio labels already wrap their
input, which is a valid association - those are left alone. Purely visual, no
layout change: only a for= attribute, plus an id where the field had none.

Idempotent: a label that already has for= is skipped.
Takes optional path prefixes to work in slices over a slow mount.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.chdir(ROOT)
SKIP = {".git", "_stage", "node_modules", ".wrangler", ".github", "cdn-cgi"}

# <label ...>text</label> immediately followed by an <input>/<select>,
# where the label has no for= and does not wrap a control itself.
PAIR = re.compile(
    r'<label(?![^>]*\bfor=)([^>]*)>((?:(?!</label>|<input|<select).)*?)</label>(\s*)<(input|select)\b([^>]*?)(/?)>',
    re.S)
HAS_ID = re.compile(r'\bid="([^"]+)"')


def pages(roots):
    out = []
    for root in roots:
        for dp, dn, fn in os.walk(root):
            dn[:] = [d for d in dn if d not in SKIP]
            for f in fn:
                if f.endswith(".html"):
                    out.append(os.path.relpath(os.path.join(dp, f), "."))
    return sorted(set(out))


def main():
    roots = sys.argv[1:] or ["."]
    files = linked = made_ids = 0
    for p in pages(roots):
        t = open(p, encoding="utf-8").read()
        counter = [0]
        stats = [0, 0]

        def rep(m):
            attrs, text, gap, tag, iattrs, close = m.groups()
            mid = HAS_ID.search(iattrs)
            if mid:
                fid = mid.group(1)
            else:
                counter[0] += 1
                fid = "cf-f%d" % counter[0]
                while ('id="%s"' % fid) in t:
                    counter[0] += 1
                    fid = "cf-f%d" % counter[0]
                iattrs = ' id="%s"%s' % (fid, iattrs)
                stats[1] += 1
            stats[0] += 1
            return '<label%s for="%s">%s</label>%s<%s%s%s>' % (
                attrs, fid, text, gap, tag, iattrs, close)

        n = PAIR.sub(rep, t)
        if n != t:
            open(p, "w", encoding="utf-8", newline="").write(n)
            files += 1
            linked += stats[0]
            made_ids += stats[1]
    print("labels linked: %d fields across %d files (%d new ids)" % (linked, files, made_ids))


if __name__ == "__main__":
    main()
