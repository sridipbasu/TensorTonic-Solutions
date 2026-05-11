import numpy as np

def clip_gradients(abc, xyz):
    g = np.asarray(abc, dtype=float)
    n = np.linalg.norm(g)

    if n == 0 or xyz <= 0 or n <= xyz:
        return g.copy()

    return g * (xyz / n)