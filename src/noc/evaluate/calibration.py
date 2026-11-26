import numpy as np


def expected_calibration_error(probs: np.ndarray, y_true: np.ndarray, n_bins: int = 15) -> float:
    """ECE trên độ tin cậy của lớp dự đoán."""
    conf = probs.max(1)
    pred = probs.argmax(1)
    correct = (pred == y_true).astype(float)
    bins = np.linspace(0, 1, n_bins + 1)
    ece = 0.0
    for lo, hi in zip(bins[:-1], bins[1:]):
        m = (conf > lo) & (conf <= hi)
        if m.any():
            ece += m.mean() * abs(correct[m].mean() - conf[m].mean())
    return float(ece)


def fit_temperature(logits: np.ndarray, y_val: np.ndarray) -> float:
    """TODO: tối ưu T trên tập validation (LBFGS hoặc grid search) để cực tiểu NLL."""
    raise NotImplementedError


def plot_reliability(probs, y_true, path, n_bins: int = 10):
    """TODO: vẽ reliability diagram, lưu vào outputs/figures."""
    raise NotImplementedError
