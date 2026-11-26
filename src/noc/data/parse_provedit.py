"""Đọc dữ liệu thô PROVEDIt -> bảng peak dạng long (1 dòng = 1 peak/allele)."""
from pathlib import Path
import pandas as pd

# Schema mong muốn của data/interim/peaks.parquet
PEAK_COLUMNS = ["sample_id", "locus", "allele", "height", "size_bp", "dye"]
META_COLUMNS = ["sample_id", "noc", "kit", "cycles", "template_ng",
                "degradation", "inhibitor", "mix_ratio", "genotype_set"]


def read_one_file(path: Path) -> pd.DataFrame:
    """TODO: đọc 1 file kết quả gọi peak (CSV từ GeneMapper/HID).
    TODO: một dòng gốc có thể chứa Allele 1..N, Height 1..N -> melt thành dạng long.
    TODO: xử lý OL (out-of-ladder), giá trị thiếu, cột thừa."""
    raise NotImplementedError


def parse_all(raw_dir: Path, kit: str):
    """TODO: duyệt raw_dir, lọc theo kit (config), gọi read_one_file + labels.parse_filename.
    Trả về (peaks_df[PEAK_COLUMNS], meta_df[META_COLUMNS])."""
    raise NotImplementedError
