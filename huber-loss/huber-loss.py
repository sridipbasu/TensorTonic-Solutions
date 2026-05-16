import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    a = np.array(y_true, dtype=float)
    b = np.array(y_pred, dtype=float)

    e = a - b
    x = np.abs(e)

    l = np.where(
        x <= delta,
        0.5 * (e ** 2),
        delta * (x - 0.5 * delta)
    )

    return float(np.mean(l))