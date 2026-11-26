import pandas as pd


def apply_threshold(peaks: pd.DataFrame, at: float) -> pd.DataFrame:
    """TODO: loại peak có height < AT."""
    raise NotImplementedError


def drop_loci(peaks: pd.DataFrame, loci: list) -> pd.DataFrame:
    """TODO: loại AMEL và các locus không dùng chung giữa mẫu."""
    raise NotImplementedError


def normalize_height(peaks: pd.DataFrame, mode: str = "log1p") -> pd.DataFrame:
    """TODO: chuẩn hóa RFU: 'log1p' | 'total' (chia tổng RFU mẫu) | 'none'.
    Lưu ý: giữ bản RFU gốc để tính đặc trưng dạng tuyệt đối (tổng RFU...)."""
    raise NotImplementedError


def filter_samples(meta: pd.DataFrame, noc_classes: list, merge_5_into_4: bool) -> pd.DataFrame:
    """TODO: giữ mẫu có NoC trong noc_classes; gộp lớp 5 -> '4+' nếu cấu hình yêu cầu."""
    raise NotImplementedError
