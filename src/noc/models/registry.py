"""Ánh xạ tên mô hình -> hàm tạo. Dùng chung cho train và benchmark."""
from .mlp import MLP
from .cnn1d import CNN1D
from .rnn import SeqRNN
from .hybrid import HybridNet

DL_MODELS = {"mlp": MLP, "cnn1d": CNN1D, "rnn": SeqRNN, "hybrid": HybridNet}
REP_OF_MODEL = {"mlp": "A", "cnn1d": "B", "rnn": "B", "hybrid": "A+B"}


def build_model(name: str, **kwargs):
    return DL_MODELS[name](**kwargs)
