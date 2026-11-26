"""Áp AT, loại locus, chuẩn hóa, lọc mẫu -> data/processed"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
from noc.utils.io import load_config, resolve
from noc.data import preprocess as P


def main():
    cfg = load_config()
    interim, out = resolve(cfg, "interim"), resolve(cfg, "processed")
    peaks, meta = pd.read_parquet(interim / "peaks.parquet"), pd.read_parquet(interim / "meta.parquet")
    d = cfg["data"]
    peaks = P.apply_threshold(peaks, d["analytical_threshold"])
    peaks = P.drop_loci(peaks, d["drop_locus"])
    meta = P.filter_samples(meta, d["noc_classes"], d["merge_5_into_4"])
    peaks = peaks[peaks.sample_id.isin(meta.sample_id)]
    peaks = P.normalize_height(peaks, d["rfu_norm"])   # TODO: giữ cả RFU gốc
    peaks.to_parquet(out / "peaks.parquet")
    meta.to_parquet(out / "meta.parquet")


if __name__ == "__main__":
    main()
