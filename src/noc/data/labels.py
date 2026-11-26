"""Trích nhãn NoC và metadata từ tên file PROVEDIt."""


def parse_filename(filename: str) -> dict:
    """
    Trả về dict metadata từ tên file, ví dụ:
        {"noc": int, "kit": str, "cycles": int, "template_ng": float,
         "degradation": str, "inhibitor": str, "mix_ratio": str, "genotype_set": str, ...}

    TODO: đọc 'PROVEDIt-Database-Naming-Convention-Laboratory-Methods' rồi viết regex/split.
    TODO: xác định trường nào là NoC, bộ người đóng góp (dùng làm nhóm khi chia dữ liệu),
          nồng độ DNA, mức suy thoái, chất ức chế, tỷ lệ trộn.
    """
    raise NotImplementedError
