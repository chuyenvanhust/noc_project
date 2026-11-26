"""Baseline: MAC, Random Forest, XGBoost. Lưu kết quả vào outputs/tables"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
from noc.utils.io import load_config, resolve
from noc.utils.seed import set_seed
from noc.models import mac, sklearn_baselines as sb
from noc.evaluate.metrics import classification_report_dict


def main():
    cfg = load_config()
    set_seed(cfg["seed"])
    proc, spl = resolve(cfg, "processed"), resolve(cfg, "splits")
    # TODO: load features_A + meta + split.csv
    # TODO: MAC -> dự đoán từ số allele mỗi locus (không cần train)
    # TODO: fit RF/XGB trên train, chọn siêu tham số bằng val, báo cáo trên test
    # TODO: lưu outputs/tables/baselines.csv
    raise NotImplementedError


if __name__ == "__main__":
    main()
