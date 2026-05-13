import numpy as np

def one_hot(abc, xyz=None):
    y = np.array(abc, dtype=int)

    if xyz is None:
        xyz = np.max(y) + 1

    if np.any(y < 0) or np.any(y >= xyz):
        raise ValueError("Invalid labels")

    res = np.zeros((len(y), xyz), dtype=float)

    res[np.arange(len(y)), y] = 1.0

    return res