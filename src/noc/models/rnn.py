import torch.nn as nn


class SeqRNN(nn.Module):
    """BiLSTM/GRU: coi mỗi locus là một bước thời gian.
    Input (N, n_loci, n_alleles)."""

    def __init__(self, in_dim: int, n_classes: int, cell="gru", hidden=128, layers=2,
                 bidirectional=True, dropout=0.3):
        super().__init__()
        # TODO: nn.GRU/nn.LSTM -> pooling theo chuỗi (mean/last/attention) -> Linear
        raise NotImplementedError

    def forward(self, x):
        # TODO
        raise NotImplementedError
