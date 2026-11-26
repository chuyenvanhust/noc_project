"""Huấn luyện một mô hình DL: python scripts/06_train_dl.py --model cnn1d --seed 42"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import argparse
from noc.utils.io import load_config, resolve
from noc.utils.seed import set_seed
from noc.models.registry import build_model, REP_OF_MODEL
from noc.train import train_model, predict_proba
from noc.evaluate.metrics import classification_report_dict
from noc.evaluate.calibration import expected_calibration_error


def run(model_name: str, seed: int, cfg: dict) -> dict:
    """Hàm dùng chung cho script này và benchmark."""
    set_seed(seed)
    rep = REP_OF_MODEL[model_name]
    # TODO: 1. load dữ liệu theo rep ('A', 'B' hoặc cả hai) + split.csv
    # TODO: 2. chuẩn hóa đặc trưng (fit scaler CHỈ trên train, rep A)
    # TODO: 3. tạo NoCDataset/DataLoader cho train/val/test
    # TODO: 4. build_model(model_name, **kwargs từ cfg['models'][model_name] + kích thước đầu vào)
    # TODO: 5. train_model(...) -> checkpoint tại outputs/checkpoints/{model_name}_seed{seed}.pt
    # TODO: 6. predict_proba trên test -> metrics + ECE -> trả về dict kết quả
    raise NotImplementedError


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=["mlp", "cnn1d", "rnn", "hybrid"])
    ap.add_argument("--seed", type=int, default=None)
    args = ap.parse_args()
    cfg = load_config()
    print(run(args.model, args.seed or cfg["seed"], cfg))


if __name__ == "__main__":
    main()
