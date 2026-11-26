# NoC Estimation in STR DNA Mixtures (PROVEDIt) – Classical Deep Learning

Khung project ước lượng số người đóng góp (NoC). Các mục `TODO` là phần cần điền.

## Cấu trúc
```
configs/      cấu hình (default.yaml)
data/raw/PROVEDIt/   <-- ĐẶT DỮ LIỆU GỐC Ở ĐÂY (không commit)
data/interim/        bảng peak đã parse
data/processed/      dữ liệu đã lọc AT + chuẩn hóa + nhãn NoC
data/splits/         file chia train/val/test (theo nhóm genotype)
src/noc/             code chính (data, features, models, evaluate, utils)
scripts/             pipeline chạy tuần tự 01 -> 07
benchmark/           chạy so sánh tất cả mô hình, nhiều seed
outputs/             checkpoints, logs, figures, tables
tests/               unit test (MAC, chống rò rỉ khi chia dữ liệu)
```

## Quy trình
```
make parse        # 01: parse PROVEDIt -> data/interim
make preprocess   # 02: áp AT, chuẩn hóa, gán nhãn NoC -> data/processed
make split        # 03: chia theo nhóm (tránh leakage) -> data/splits
make features     # 04: biểu diễn A (vector) và B (ma trận locus x allele)
make baselines    # 05: MAC, RF, XGBoost
make train MODEL=cnn1d   # 06: mlp | cnn1d | rnn | hybrid
make benchmark    # chạy tất cả, nhiều seed -> benchmark/results
make analyze      # 07: calibration, phân tích lỗi, giải thích
make test
```

## Việc cần làm đầu tiên
1. Đặt dữ liệu vào `data/raw/PROVEDIt/`.
2. Đọc naming convention, hoàn thiện `src/noc/data/labels.py`.
3. Hoàn thiện `parse_provedit.py` (bắt đầu với 1 thư mục nhỏ).
4. Xem phân bố số mẫu theo NoC trước khi chốt `noc_classes`.
