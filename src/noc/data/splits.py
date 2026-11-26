"""Chia dữ liệu THEO NHÓM để tránh rò rỉ (cùng bộ người đóng góp không xuất hiện ở nhiều tập)."""
import pandas as pd


def make_group_split(meta: pd.DataFrame, group_col: str, ratios=(0.70, 0.15, 0.15), seed: int = 42) -> pd.DataFrame:
    """TODO: trả về DataFrame [sample_id, split] với split ∈ {train,val,test}.
    Gợi ý: sklearn GroupShuffleSplit; cố gắng giữ phân bố NoC (StratifiedGroupKFold)."""
    raise NotImplementedError


def make_group_kfold(meta: pd.DataFrame, group_col: str, n_folds: int = 5, seed: int = 42) -> pd.DataFrame:
    """TODO: StratifiedGroupKFold -> cột 'fold' cho từng sample_id."""
    raise NotImplementedError


def assert_no_leakage(meta: pd.DataFrame, split_df: pd.DataFrame, group_col: str) -> None:
    """TODO: kiểm tra mỗi nhóm chỉ nằm trong đúng một split; raise AssertionError nếu vi phạm."""
    raise NotImplementedError
