import torch.nn as nn


class MLP(nn.Module):
    """MLP cho biểu diễn A."""

    def __init__(self, in_dim: int, n_classes: int, hidden=(256, 128), dropout=0.3):
        super().__init__()
        # TODO: Linear -> BatchNorm -> ReLU -> Dropout (lặp theo hidden) -> Linear(n_classes)
        raise NotImplementedError

    def forward(self, x):
        # TODO
        raise NotImplementedError
