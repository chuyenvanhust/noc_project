"""Chạy tất cả mô hình x nhiều seed trên CÙNG split, tổng hợp mean ± std.
Kết quả: benchmark/results/benchmark.csv và benchmark_summary.csv"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "scripts"))
import importlib
import pandas as pd
from noc.utils.io import load_config, ROOT

MODELS = ["mlp", "cnn1d", "rnn", "hybrid"]      # TODO: bỏ 'hybrid' nếu không làm
BASELINES = ["mac", "rf", "xgboost"]            # TODO: nối vào kết quả từ 05_train_baselines


def main():
    cfg = load_config()
    train_dl = importlib.import_module("06_train_dl")
    rows = []
    for m in MODELS:
        for seed in cfg["seeds"]:
            res = train_dl.run(m, seed, cfg)   # TODO: dict {accuracy, macro_f1, ece, ...}
            rows.append({"model": m, "seed": seed, **{k: v for k, v in res.items() if isinstance(v, float)}})
    # TODO: thêm baseline (MAC không phụ thuộc seed; RF/XGB lặp theo seed)
    df = pd.DataFrame(rows)
    out = ROOT / "benchmark" / "results"
    df.to_csv(out / "benchmark.csv", index=False)
    summary = df.groupby("model").agg(["mean", "std"]).drop(columns="seed")
    summary.to_csv(out / "benchmark_summary.csv")
    print(summary)
    # TODO: (tùy chọn) đo thêm thời gian train, số tham số, thời gian suy luận


if __name__ == "__main__":
    main()
