"""Vòng huấn luyện dùng chung cho các mô hình DL."""
import numpy as np


def train_model(model, train_loader, val_loader, cfg: dict, class_weights=None, ckpt_path=None) -> dict:
    """TODO:
      - device (cfg['train']['device']), loss CrossEntropy(weight=class_weights)
      - Adam(lr, weight_decay), (tùy chọn) scheduler
      - vòng epoch: train -> validate (macro-F1 / val loss)
      - early stopping theo patience, lưu checkpoint tốt nhất vào ckpt_path
      - trả về history {train_loss, val_loss, val_macro_f1}
    """
    raise NotImplementedError


@np.errstate(all="ignore")
def predict_proba(model, loader, device="cpu") -> np.ndarray:
    """TODO: trả về xác suất softmax shape (N, n_classes)."""
    raise NotImplementedError
