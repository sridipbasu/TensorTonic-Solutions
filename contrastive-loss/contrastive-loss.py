import numpy as np

def contrastive_loss(a: list, b: list, y: list, margin: float = 1.0, reduction: str = "mean") -> float:
    """
    Returns the loss as a float.
    """
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    y = np.array(y, dtype=float)

    if a.ndim == 1:
        a = a.reshape(1, -1)
        b = b.reshape(1, -1)

    abc = np.linalg.norm(a - b, axis=1)
    xyz = y * abc ** 2 + (1 - y) * np.maximum(0, margin - abc) ** 2

    if reduction == "sum":
        return float(np.sum(xyz))
    return float(np.mean(xyz))