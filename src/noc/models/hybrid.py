import torch.nn as nn


class HybridNet(nn.Module):
    """(Tùy chọn) Nhánh CNN cho B + nhánh MLP cho A, nối ở lớp cuối."""

    def __init__(self, feat_dim: int, in_channels: int, n_classes: int):
        super().__init__()
        # TODO: self.cnn, self.mlp, self.head
        raise NotImplementedError

    def forward(self, x_matrix, x_feat):
        # TODO
        raise NotImplementedError
