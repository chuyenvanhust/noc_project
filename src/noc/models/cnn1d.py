import torch.nn as nn


class CNN1D(nn.Module):
    """CNN 1D cho biểu diễn B. Input (N, n_loci, n_alleles).
    TODO: chọn hướng quét: (a) kênh = locus, trượt dọc trục allele;
          (b) kênh = allele, trượt dọc chuỗi locus. Thử và so sánh."""

    def __init__(self, in_channels: int, n_classes: int, channels=(32, 64, 128), kernel=3, dropout=0.3):
        super().__init__()
        # TODO: [Conv1d -> BN -> ReLU -> MaxPool] x len(channels) -> GlobalPool -> Dropout -> Linear
        raise NotImplementedError

    def forward(self, x):
        # TODO
        raise NotImplementedError
