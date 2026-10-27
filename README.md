# Từ điển thuật ngữ Anh–Việt · Hình học giải tích

Website tĩnh (HTML + CSS + JavaScript thuần), không cần máy chủ, không cần cài đặt. 284 mục từ. Trang đầu là “Quy ước & nguồn”; gõ vào ô tìm kiếm (EN hoặc VI, không cần dấu) để hiện gợi ý, bấm gợi ý hoặc nhấn Enter để mở trang riêng của thuật ngữ (định nghĩa, ví dụ, mô hình 3D với các mặt bậc hai, liên quan, nguồn, danh sách cùng mục). Có thêm bảng tra A–Z hai chiều, lọc theo chương/mục, chế độ sáng/tối, in / lưu PDF, flashcard.

## Các file

| File | Việc của file |
|---|---|
| `index.html` | Giao diện và mã chạy của website |
| `data.js` | Toàn bộ 284 mục từ (tự sinh, không sửa tay) |
| `config.js` | **Thông tin nhóm** (tên lớp, giảng viên, học kỳ, 10 thành viên) — file duy nhất bạn cần sửa |
| `favicon.svg`, `404.html`, `.nojekyll` | Biểu tượng tab, trang báo lỗi, tắt Jekyll của GitHub |
| `tools/` | Script dựng lại `data.js` khi nội dung từ điển thay đổi |

Mở thử trên máy: bấm đúp `index.html` (chạy được cả khi không có mạng, chỉ khác phông chữ).

## Đưa lên GitHub Pages (khoảng 5 phút, dùng trình duyệt)

1. Đăng nhập https://github.com (chưa có tài khoản thì đăng ký miễn phí).
2. Bấm **+** ở góc trên phải → **New repository**.
   - Repository name: ví dụ `tu-dien-hhgt` (chỉ dùng chữ thường, số, dấu gạch ngang).
   - Chọn **Public** (GitHub Pages miễn phí cần repo công khai).
   - Bấm **Create repository**.
3. Trong repo mới, bấm **uploading an existing file**. Giải nén file zip này ra máy, rồi **kéo toàn bộ file và thư mục bên trong** (`index.html`, `data.js`, `config.js`, `favicon.svg`, `404.html`, `.nojekyll`, `tools`, `README.md`) thả vào khung upload. Lưu ý: kéo *nội dung* của thư mục, không kéo cả thư mục bọc ngoài. File `.nojekyll` bị ẩn trên Windows/macOS; nếu không thấy, bỏ qua cũng được.
4. Kéo xuống cuối trang, bấm **Commit changes**.
5. Vào **Settings** → **Pages** (menu bên trái).
   - Source: **Deploy from a branch**.
   - Branch: **main**, thư mục **/ (root)** → **Save**.
6. Đợi 1–2 phút, tải lại trang Settings → Pages. GitHub hiện địa chỉ:
   `https://<tên-tài-khoản>.github.io/tu-dien-hhgt/`
   Đó là link nộp bài. Mở thử trên điện thoại và máy tính.

## Điền thông tin nhóm

1. Trong repo, bấm file `config.js` → biểu tượng cây bút (Edit).
2. Thay các chữ trong `[ngoặc vuông]` bằng thông tin thật (giữ nguyên dấu nháy kép `"` và dấu phẩy cuối dòng). Dòng nào để `""` thì website tự ẩn.
3. Bấm **Commit changes**. Sau 1–2 phút website tự cập nhật (nếu chưa thấy, nhấn Ctrl+F5).

## Khi nội dung từ điển thay đổi

Dựng lại `data.js` từ file dữ liệu đã chốt rồi tải đè `data.js` lên repo:

```
python3 tools/build_data.py merged.json index.json data.js 2026-10-27
```

(`merged.json` và `index.json` do quy trình dựng file Word sinh ra; ngày ở cuối là ngày hiện trên chân trang.) Nếu chỉ sửa vài chữ, có thể nhờ Claude cập nhật rồi gửi lại `data.js` mới.

## Tương thích

Chrome, Edge, Firefox, Safari (macOS, iOS), Android; màn hình từ 320 px (điện thoại nhỏ) đến 4K. Tự theo chế độ sáng/tối của hệ điều hành, có nút đổi tay. Danh sách đã lưu và tiến độ flashcard nằm trong trình duyệt của từng người xem.
