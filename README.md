# Từ điển thuật ngữ Anh–Việt · Hình học giải tích (bản 4)

Website tĩnh (HTML + CSS + JavaScript thuần), không cần máy chủ. 284 mục từ, 205 hình minh họa SVG, vectơ có mũi tên trên đầu ký hiệu, chính tả theo giáo trình (afin, elip, hypebol…). Bố cục kiểu từ điển trực tuyến: ô tìm kiếm lớn ở trang chủ, “Quy ước & nguồn” ngay bên dưới, trang riêng cho từng thuật ngữ (định nghĩa EN/VI, ví dụ, hình minh họa, mô hình 3D cho mặt bậc hai, liên quan, nguồn), bảng tra A–Z hai chiều, flashcard, chế độ sáng/tối, in / lưu PDF.

## Có gì mới ở bản 4

- Bảng màu mới: đỏ đô (#8B1E3F) làm màu chủ đạo, xanh lam (#1D6FD8) làm màu nhấn; nền trắng.
- Giao diện theo kiểu từ điển trực tuyến: thanh đầu trang cố định, ô tìm kiếm có nút kính lúp, trang thuật ngữ có từ khóa lớn, nút phát âm, nhãn VI/EN cho từng khối định nghĩa.
- Logo riêng (elip có hai tiêu điểm trên hệ trục) và hình nền toán học (lưới tọa độ, elip, hypebol, parabol, công thức) ở trang chủ.
- Sửa lỗi chữ tiếng Việt bị vỡ dấu (ví dụ “Nguô`n”): phông chữ nay được nhúng thẳng vào `index.html`, nên **không còn cần thư mục `fonts/` và file `fonts.css`**.

## Các file

| File | Việc của file |
|---|---|
| `index.html` | Giao diện, mã chạy và phông chữ (đã nhúng) |
| `data.js` | Toàn bộ 284 mục từ (tự sinh, không sửa tay) |
| `figs.js` | 205 hình minh họa SVG, gắn theo số mục (tự sinh) |
| `config.js` | **Thông tin nhóm** (lớp, giảng viên, học kỳ, 10 thành viên) — file duy nhất cần sửa tay |
| `favicon.svg`, `404.html`, `.nojekyll` | Logo tab, trang báo lỗi, tắt Jekyll của GitHub |
| `tools/` | Script dựng lại `data.js` khi nội dung từ điển thay đổi |

Quy ước ký hiệu trong dữ liệu: vectơ đánh dấu `⟦AB⟧`, `⟦u⟧`, `⟦0⟧`…; trang tự vẽ mũi tên lên đầu. Chỉ số dưới viết `⟦e₁⟧` hoặc `X_cũ`.

Mở thử trên máy: bấm đúp `index.html` (chạy được cả khi không có mạng).

## Cập nhật lên repo đã có (cách ngắn nhất)

1. Giải nén file zip ra máy.
2. Vào repo trên GitHub → **Add file → Upload files**, kéo các file sau vào: `index.html`, `data.js`, `figs.js`, `favicon.svg`, `404.html`, `README.md`, thư mục `tools` (file trùng tên sẽ bị ghi đè). **Nếu `config.js` trên repo đã điền thông tin nhóm thì không kéo `config.js` mới lên.** Nếu chưa điền, kéo luôn cũng được.
3. Bấm **Commit changes**. Đợi 1–2 phút rồi nhấn Ctrl+F5 để xem bản mới.
4. Dọn repo (không bắt buộc): xóa thư mục `fonts`, file `fonts.css`, file `tools/assemble.py` và các file `.bak` nếu còn. Mở từng mục → biểu tượng thùng rác (hoặc ba chấm → Delete) → Commit changes.

## Làm lại từ đầu trên repo mới

1. https://github.com → **+** → **New repository** (tên ví dụ `tu-dien-hhgt`, chọn **Public**).
2. **uploading an existing file** → kéo toàn bộ nội dung đã giải nén vào → **Commit changes**.
3. **Settings → Pages** → Source: *Deploy from a branch*, Branch: `main`, thư mục `/ (root)` → **Save**.
4. Sau 1–2 phút GitHub hiện địa chỉ `https://<tên-tài-khoản>.github.io/tu-dien-hhgt/`.

## Điền thông tin nhóm

1. Trong repo, bấm `config.js` → biểu tượng cây bút (Edit).
2. Thay các chữ trong `[ngoặc vuông]` bằng thông tin thật (giữ dấu nháy kép `"` và dấu phẩy cuối dòng). Dòng nào để `""` thì website tự ẩn.
3. **Commit changes**; sau 1–2 phút website tự cập nhật.

## Khi nội dung từ điển thay đổi

```
python3 tools/build_data.py merged.json index.json data.js 2026-11-04
```

(`merged.json` và `index.json` do quy trình dựng file Word sinh ra; ngày ở cuối hiện trên chân trang.) Nếu chỉ sửa vài chữ, có thể nhờ Claude cập nhật rồi gửi lại `data.js` mới.

## Tương thích

Chrome, Edge, Firefox, Safari (macOS, iOS), Android; màn hình từ 320 px đến 4K. Tự theo chế độ sáng/tối của hệ điều hành, có nút đổi tay. Danh sách đã lưu và tiến độ flashcard nằm trong trình duyệt của từng người xem.
