"""Chia train/val/test + group k-fold theo nhóm -> data/splits"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src"))

import pandas as pd
from noc.utils.io import load_config, resolve
from noc.data import splits as S


def main():
    cfg = load_config()
    proc, out = resolve(cfg, "processed"), resolve(cfg, "splits")
    meta = pd.read_parquet(proc / "meta.parquet")
    g, sp = cfg["split"]["group_by"], cfg["split"]
    split_df = S.make_group_split(meta, g, (sp["train"], sp["val"], sp["test"]), cfg["seed"])
    S.assert_no_leakage(meta, split_df, g)
    split_df.to_csv(out / "split.csv", index=False)
    fold_df = S.make_group_kfold(meta, g, sp["n_folds"], cfg["seed"])
    fold_df.to_csv(out / "folds.csv", index=False)


if __name__ == "__main__":
    main()
