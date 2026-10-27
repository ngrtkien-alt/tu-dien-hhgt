#!/usr/bin/env python3
"""Tạo data.js cho website từ merged.json + index.json (bản Word đã chốt).
Dùng:  python3 tools/build_data.py <merged.json> <index.json> <data.js> [YYYY-MM-DD]
"""
import json, sys, datetime

merged, index, out = sys.argv[1:4]
stamp = sys.argv[4] if len(sys.argv) > 4 else datetime.date.today().isoformat()
m = json.load(open(merged, encoding="utf-8"))
ix = json.load(open(index, encoding="utf-8"))

CONV_VI = [
 ("Cấu trúc mục", "Mỗi mục gồm: tên EN → tên VI, định nghĩa EN/VI, ví dụ EN/VI, thuật ngữ liên quan, nguồn. Biến thể của cùng một thuật ngữ nằm trong ngoặc đơn, ngăn cách bằng dấu chấm phẩy. Từ loại (n, n phr, adj) của các mục Chương 2 ghi cạnh tên EN."),
 ("Đánh số", "Đánh số liên tục từ 1 đến {N}: Chương 1 gồm mục {R1}, Chương 2 gồm mục {R2}, Chương 3 gồm mục {R3}. Trong phần “Liên quan” và “Xem thêm”, số mục dạng #N là liên kết bấm được; thuật ngữ chưa có mục riêng hiển thị bằng chữ xám, không liên kết."),
 ("Chính tả", "Thống nhất toàn bộ phần tiếng Việt: vectơ, affine, ellipse, hyperbola, parabola (cùng họ ellipsoid, hyperboloid, paraboloid). “Mục tiêu” = frame; “hệ tọa độ” = coordinate system."),
 ("Ký hiệu", "Vectơ AB viết là AB; vectơ không viết là 0. Tích vô hướng u·v; tích hữu hướng u ∧ v = [u, v]; tích hỗn tạp D(u, v, w) = [u, v, w]; đạo hàm riêng f′x = ∂f/∂x."),
 ("Nguồn", "“Giáo trình Chương 2” là tài liệu của học phần Hình học giải tích cho Chương 2. “Tiểu luận Hình học giải tích - 2511MATH1405104 - Nhóm 4” là tài liệu học phần do các anh chị khóa trước soạn theo giao của thầy, đã được thầy đồng ý cho sử dụng (số trang theo bản in của tiểu luận). Downing (2009) là Dictionary of Mathematics Terms, 3rd ed., Barron’s (số trang theo bản in). Smith & Gale (1904): P. F. Smith và A. S. Gale, Introduction to Analytic Geometry, Ginn & Company, Boston; số trang là số trang in trong sách. Vaisman (1997), Pogorelov (1980), Agnew (1962), Efimov, Axler, James & James (1992), Gallier (2001) là các giáo trình và từ điển tham khảo."),
]
CONV_EN = [
 ("Entry layout", "Each entry gives: EN term → VI term, EN/VI definition, EN/VI example, related terms and sources. Variants of one term sit in parentheses, separated by semicolons. Part of speech (n, n phr, adj) for Chapter 2 entries is shown next to the EN term."),
 ("Numbering", "Entries are numbered continuously from 1 to {N}: Chapter 1 = entries {R1}, Chapter 2 = entries {R2}, Chapter 3 = entries {R3}. In “Related” and “See also”, #N is a clickable link; terms without an entry of their own appear in grey and are not linked."),
 ("Spelling", "Vietnamese terms follow one spelling throughout: vectơ, affine, ellipse, hyperbola, parabola (and ellipsoid, hyperboloid, paraboloid). “Mục tiêu” = frame; “hệ tọa độ” = coordinate system."),
 ("Notation", "Vector AB is written AB; the zero vector is 0. Dot product u·v; cross product u ∧ v = [u, v]; triple product D(u, v, w) = [u, v, w]; partial derivative f′x = ∂f/∂x."),
 ("Sources", "“Giáo trình Chương 2” is the course text for Chapter 2. “Tiểu luận Hình học giải tích - 2511MATH1405104 - Nhóm 4” is a course document written by earlier cohorts at the lecturer’s assignment and approved by him for use (page numbers follow the printed essay). Downing (2009) is Dictionary of Mathematics Terms, 3rd ed., Barron’s (printed page numbers). Smith & Gale (1904): P. F. Smith and A. S. Gale, Introduction to Analytic Geometry, Ginn & Company, Boston (printed page numbers). Vaisman (1997), Pogorelov (1980), Agnew (1962), Efimov, Axler, James & James (1992) and Gallier (2001) are reference textbooks and dictionaries."),
]

E = m["entries"]
assert [e["gid"] for e in E] == list(range(1, len(E) + 1)), "gid không liên tục"
rng = {}
for c in (1, 2, 3):
    ns = [e["gid"] for e in E if e["ch"] == c]
    rng[c] = f"{ns[0]}–{ns[-1]}"
    assert ns == list(range(ns[0], ns[-1] + 1))
fmt = lambda s: s.format(N=len(E), R1=rng[1], R2=rng[2], R3=rng[3])

chapters = []
for c in ("1", "2", "3"):
    cv, ce = m["ch_titles"][c]
    secs = []
    for i, (sv, se) in enumerate(m["sec_titles"][c], 1):
        s = {"id": f"{c}.{i}", "titleVi": sv, "titleEn": se}
        if c == "3" and m.get("sec_note3", {}).get(str(i)):
            s["note"] = m["sec_note3"][str(i)]
        secs.append(s)
    chapters.append({"id": int(c), "titleVi": cv, "titleEn": ce, "sections": secs})

valid = {e["gid"] for e in E}
entries = []
for e in E:
    rel = []
    for r in e["rel"]:
        tg = r.get("target")
        assert tg is None or tg in valid, (e["gid"], r)
        rel.append({"t": r["text"], "n": tg})
    for g in e["see"]:
        assert g in valid and g != e["gid"], (e["gid"], g)
    entries.append({
        "n": e["gid"], "chapter": e["ch"], "section": f'{e["ch"]}.{e["sec"]}',
        "en": e["en"], "vi": e["vi"], "pos": e.get("pos") or "",
        "defEn": e["defEN"], "defVi": e["defVI"],
        "exEn": e.get("exEN") or "", "exVi": e.get("exVI") or "",
        "related": rel, "seeAlso": e["see"], "source": e.get("src") or "",
    })

# phiên bản các dòng tra cứu: [thuật ngữ, tương ứng, [số mục]]
lk = lambda side: [[r["term"], r["cp"], r["nums"]] for g in side for r in g["rows"]]
data = {
    "version": stamp,
    "chapters": chapters,
    "entries": entries,
    "lookupEnVi": lk(ix["en"]),
    "lookupViEn": lk(ix["vi"]),
    "conventions": {
        "vi": [{"label": a, "text": fmt(b)} for a, b in CONV_VI],
        "en": [{"label": a, "text": fmt(b)} for a, b in CONV_EN],
    },
}
for side in ("lookupEnVi", "lookupViEn"):
    for t, cp, ns in data[side]:
        assert all(n in valid for n in ns), (t, ns)
body = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
if out.endswith(".js"):
    body = "/* Tự sinh bởi tools/build_data.py — không sửa tay. */\nwindow.HHGT_DATA=" + body + ";\n"
open(out, "w", encoding="utf-8").write(body)
print("OK", len(entries), "mục;", len(data["lookupEnVi"]), "EN;", len(data["lookupViEn"]), "VI;",
      sum(len(e["related"]) for e in entries), "liên quan;", sum(1 for e in entries for r in e["related"] if r["n"] is None), "không liên kết")
