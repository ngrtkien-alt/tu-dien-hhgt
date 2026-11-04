#!/usr/bin/env python3
"""Đổi chính tả phần tiếng Việt theo sách giáo khoa: afin, elip, hypebol, parabol, elipxoit, hypeboloit, paraboloit.
Dùng: python3 tools/spell.py merged_src.json merged.json"""
import json, re, sys
MAP = [  # thứ tự quan trọng: từ dài trước
    ("ellipsoid", "elipxoit"), ("hyperboloid", "hypeboloit"), ("paraboloid", "paraboloit"),
    ("elliptic", "eliptic"), ("hyperbolic", "hypebolic"),
    ("ellipse", "elip"), ("hyperbola", "hypebol"), ("parabola", "parabol"), ("affine", "afin"),
]
PAT = re.compile("|".join(a for a, _ in MAP), re.I)
LOOK = dict(MAP)
def sp(s):
    if not isinstance(s, str): return s
    def f(m):
        w = m.group(0); r = LOOK[w.lower()]
        return r.capitalize() if w[0].isupper() else r
    return PAT.sub(f, s)
if __name__ == "__main__":
    m = json.load(open(sys.argv[1], encoding="utf-8"))
    n = 0
    for e in m["entries"]:
        for k in ("vi", "defVI", "exVI"):
            v = sp(e[k]); n += v != e[k]; e[k] = v
        if e.get("vi_surf"): e["vi_surf"] = [sp(x) for x in e["vi_surf"]]
    for c in m["ch_titles"]: m["ch_titles"][c][0] = sp(m["ch_titles"][c][0])
    for c in m["sec_titles"]: m["sec_titles"][c] = [[sp(a), b] for a, b in m["sec_titles"][c]]
    json.dump(m, open(sys.argv[2], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("trường đã đổi:", n)
