from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[3]


def load_config(path: str = "configs/default.yaml") -> dict:
    with open(ROOT / path) as f:
        return yaml.safe_load(f)


def resolve(cfg: dict, key: str) -> Path:
    """Trả về đường dẫn tuyệt đối cho cfg['paths'][key]."""
    p = ROOT / cfg["paths"][key]
    p.mkdir(parents=True, exist_ok=True)
    return p
