import numpy as np
from torch.utils.data import Dataset


class NoCDataset(Dataset):
    """Dataset cho cả hai biểu diễn.
    rep='A': X shape (N, F)               - vector đặc trưng
    rep='B': X shape (N, n_loci, n_alleles) - ma trận locus x allele
    """

    def __init__(self, X: np.ndarray, y: np.ndarray):
        # TODO: chuyển sang tensor; thêm transform/augmentation nếu cần
        self.X, self.y = X, y

    def __len__(self):
        return len(self.y)

    def __getitem__(self, i):
        # TODO: trả về (x, y) dạng torch.Tensor (float32, long)
        raise NotImplementedError


def class_weights(y: np.ndarray, n_classes: int) -> np.ndarray:
    """TODO: trọng số nghịch đảo tần suất lớp để xử lý mất cân bằng."""
    raise NotImplementedError
