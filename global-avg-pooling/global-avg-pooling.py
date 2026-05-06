import numpy as np

def global_avg_pool(abc):
    x = np.array(abc, dtype=float)

    if x.ndim == 3:
        return np.mean(x, axis=(1, 2))

    if x.ndim == 4:
        return np.mean(x, axis=(2, 3))

    raise ValueError("inv shape")