import pandas as pd


def error_by_factor(meta: pd.DataFrame, y_true, y_pred, factor: str) -> pd.DataFrame:
    """TODO: accuracy theo nhóm của 'factor' (template_ng, degradation, inhibitor, mix_ratio, noc).
    Gợi ý: gộp template_ng thành các bin trước khi group."""
    raise NotImplementedError


def confusion_focus(y_true, y_pred, a: int = 3, b: int = 4):
    """TODO: thống kê nhầm lẫn riêng giữa NoC=a và NoC=b."""
    raise NotImplementedError
