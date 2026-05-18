import numpy as np

def chi2_independence(C):
    a = np.array(C, dtype=float)

    r = np.sum(a, axis=1)
    c = np.sum(a, axis=0)
    t = np.sum(a)

    e = np.outer(r, c) / t

    x = np.sum((a - e) ** 2 / e)

    return float(x), e