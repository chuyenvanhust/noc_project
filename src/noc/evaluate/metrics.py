import numpy as np
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def classification_report_dict(y_true, y_pred, n_classes: int) -> dict:
    y_true, y_pred = np.asarray(y_true), np.asarray(y_pred)
    labels = list(range(n_classes))
    per_class_acc = {
        int(c): float((y_pred[y_true == c] == c).mean()) if (y_true == c).any() else float("nan")
        for c in labels
    }
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", labels=labels, zero_division=0)),
        "per_class_acc": per_class_acc,
        "confusion_matrix": confusion_matrix(y_true, y_pred, labels=labels).tolist(),
    }
