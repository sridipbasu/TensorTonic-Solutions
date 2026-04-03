import numpy as np

def dropout(x, p=0.5, rng=None):
    x = np.array(x)  # ensure ndarray

    if p == 0.0:
        return x.copy(), np.ones_like(x)

    rand = rng.random(x.shape) if rng is not None else np.random.random(x.shape)

    kp_mask = rand >= p
    scale = 1.0 / (1.0 - p)

    dropout_p = kp_mask.astype(x.dtype) * scale
    op = x * dropout_p

    return op, dropout_p