import numpy as np

def apply_causal_mask(abc, xyz=-1e9):
    t = abc.shape[-1]
    m = np.triu(np.ones((t, t), dtype=bool), k=1)
    res = np.array(abc, dtype=float, copy=True)
    res[..., m] = xyz
    return res