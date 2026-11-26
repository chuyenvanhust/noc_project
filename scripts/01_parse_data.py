"""Parse PROVEDIt thô -> data/interim/peaks.parquet, meta.parquet"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

from noc.utils.io import load_config, resolve
from noc.data.parse_provedit import parse_all


def main():
    cfg = load_config()
    raw, interim = resolve(cfg, "raw"), resolve(cfg, "interim")
    peaks, meta = parse_all(raw, cfg["data"]["kit"])   # TODO trong parse_provedit.py
    peaks.to_parquet(interim / "peaks.parquet")
    meta.to_parquet(interim / "meta.parquet")
    print("Phân bố NoC:\n", meta["noc"].value_counts().sort_index())   # kiểm tra trước khi chốt số lớp


if __name__ == "__main__":
    main()
