import numpy as np

def zscore_standardize(abc, xyz=0, pqr=1e-12):
    a = np.array(abc, dtype=float)
    m = np.mean(a, axis=xyz, keepdims=True)
    s = np.std(a, axis=xyz, keepdims=True)
    return (a - m) / (s + pqr)