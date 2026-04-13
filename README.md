# IAI Courses Homepage

Landing page cho các học phần của Viện Trí tuệ nhân tạo, Trường Đại học Công nghệ, ĐHQGHN.

## Cấu trúc

- `index.html` — trang chủ
- `assets/styles.css` — giao diện
- `assets/courses.js` — dữ liệu các học phần
- `assets/app.js` — render dữ liệu ra giao diện
- `preview.py` — server preview local

## Preview local

```bash
.conda/bin/python preview.py        # mặc định port 8080
.conda/bin/python preview.py 3000   # chỉ định port
```

Server tự động tắt cache và in ra các file thay đổi khi chỉnh sửa.

## Thêm một học phần mới

Thêm object vào mảng `window.COURSES` trong `assets/courses.js`:

```js
{
  slug: "ten-mon-hoc",
  title: "Tên môn học",
  englishTitle: "Course Name",
  year: 1,        // năm học trong chương trình (1, 2, 3, 4)
  semester: 2,    // học kỳ trong năm (1 hoặc 2)
  courseUrl: "/ten-mon-hoc/",
  repoUrl: "https://github.com/uet-iai-course/ten-mon-hoc"
}
```

Sau đó push repo `uet-iai-course.github.io`.

## Danh sách học phần hiện tại

| Môn học | Năm | Kỳ |
|---|---|---|
| Tư duy tính toán | 1 | 1 |
| Phương pháp luận lập trình | 1 | 2 |
| Lập trình xử lý dữ liệu | 2 | 1 |
| Kỹ nghệ hệ thống Trí tuệ nhân tạo | 2 | 2 |
| Học máy | 2 | 2 |
