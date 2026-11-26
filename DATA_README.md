# Thư mục dữ liệu

Đặt dữ liệu gốc vào `data/raw/PROVEDIt/` (tải từ https://lftdi.camden.rutgers.edu/provedit/):
- file kết quả gọi peak (CSV) của các mẫu hỗn hợp,
- file genotype của người đóng góp (nếu cần để kiểm tra nhãn),
- tài liệu Naming Convention / Laboratory Methods (để viết `labels.py`).

Các thư mục còn lại do script sinh ra, không commit:
- `interim/`   : bảng peak/meta đã parse
- `processed/` : sau lọc AT, chuẩn hóa, đặc trưng A và B
- `splits/`    : split.csv, folds.csv
