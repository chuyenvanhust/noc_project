"""Tạo biểu diễn A (vector) và B (ma trận) -> data/processed"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import numpy as np, pandas as pd
from noc.utils.io import load_config, resolve
from noc.features import handcrafted, matrix


def main():
    cfg = load_config()
    proc = resolve(cfg, "processed")
    peaks, meta = pd.read_parquet(proc / "peaks.parquet"), pd.read_parquet(proc / "meta.parquet")
    feat = handcrafted.build_features(peaks, meta)             # TODO
    feat.to_parquet(proc / "features_A.parquet")
    # TODO: allele_index nên suy ra từ thông tin kit hoặc tập train
    idx = matrix.build_allele_index(peaks)
    X, ids = matrix.build_matrices(peaks, idx, loci_order=list(idx.keys()))
    np.savez_compressed(proc / "matrix_B.npz", X=X, sample_ids=np.array(ids))


if __name__ == "__main__":
    main()
