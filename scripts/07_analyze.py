"""Calibration, phân tích lỗi, giải thích -> outputs/figures, outputs/tables"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from noc.utils.io import load_config
from noc.evaluate import calibration, error_analysis, explain


def main():
    cfg = load_config()
    # TODO: load dự đoán test đã lưu (probs, y_true) của mô hình tốt nhất
    # TODO: reliability diagram + temperature scaling (fit T trên val)
    # TODO: error_by_factor theo template_ng, degradation, inhibitor, mix_ratio
    # TODO: confusion_focus(NoC 3 vs 4)
    # TODO: (tùy chọn) permutation importance / saliency
    raise NotImplementedError


if __name__ == "__main__":
    main()
