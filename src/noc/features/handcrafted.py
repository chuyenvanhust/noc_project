"""Biểu diễn A: vector đặc trưng tổng hợp."""
import numpy as np
import pandas as pd


def build_features(peaks: pd.DataFrame, meta: pd.DataFrame) -> pd.DataFrame:
    """Trả về DataFrame, index = sample_id, mỗi cột là một đặc trưng.

    TODO (chọn/bổ sung):
      - số allele mỗi locus; max, mean, std số allele; MAC = ceil(max/2)
      - số locus có >=3, >=4, >=5, >=6 allele
      - tổng/trung bình/std/median RFU; số peak tổng
      - PHR: thống kê tỷ lệ chiều cao giữa các cặp peak trong locus
      - độ dốc suy thoái: hệ số hồi quy RFU ~ size_bp
      - số peak ở vị trí stutter (nằm cách allele cao hơn 1 repeat, RFU thấp)
      - số locus có 0-1 allele (dấu hiệu dropout)
    KHÔNG dùng cột meta (template, degradation...) làm đặc trưng - chỉ để phân tích lỗi.
    """
    raise NotImplementedError
