"""Biểu diễn B: ma trận locus x allele giữ cấu trúc."""
import numpy as np
import pandas as pd


def build_allele_index(peaks: pd.DataFrame) -> dict:
    """TODO: {locus: [danh sách allele có thể có]} -> xác định kích thước trục allele.
    Tính TRÊN TẬP TRAIN hoặc từ thông tin kit để tránh rò rỉ."""
    raise NotImplementedError


def build_matrices(peaks: pd.DataFrame, allele_index: dict, loci_order: list) -> tuple:
    """TODO: trả về (X, sample_ids) với X shape (N, n_loci, max_alleles), giá trị = RFU chuẩn hóa.
    Gợi ý: sắp xếp locus theo kênh màu + kích thước để CNN/RNN tận dụng thứ tự."""
    raise NotImplementedError
