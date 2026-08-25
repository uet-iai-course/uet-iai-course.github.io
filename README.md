# IAI Courses Homepage

Landing page cho các học phần của Viện Trí tuệ nhân tạo, Trường Đại học Công nghệ, ĐHQGHN — <https://courses.iaidev.com/>.

Site tĩnh (HTML/CSS/JS thuần), deploy bằng GitHub Pages từ nhánh `main`.

## Cấu trúc

- `index.html` — khung trang
- `assets/courses.js` — dữ liệu học phần (nguồn duy nhất)
- `assets/app.js` — render dữ liệu ra `#course-grid`
- `assets/styles.css` — giao diện
- `preview.py` — server preview local
- `CNAME` — domain `courses.iaidev.com` (không xoá)

## Preview local

```bash
python3 preview.py        # http://localhost:8080
python3 preview.py 3000   # chỉ định port
```

## Thêm / sửa học phần

Sửa mảng `window.COURSES` trong `assets/courses.js` theo mẫu các entry có sẵn, giữ thứ tự theo năm → học kỳ. Xem lại bằng `preview.py` rồi push lên `main`.
