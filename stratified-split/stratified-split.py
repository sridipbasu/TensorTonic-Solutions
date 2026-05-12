import numpy as np

def stratified_split(X, y, test_size=0.2, rng=None):
    a = np.array(X)
    b = np.array(y)

    if rng is None:
        rng = np.random.default_rng()

    tr = []
    te = []

    for i in np.unique(b):
        idx = np.where(b == i)[0].copy()

        rng.shuffle(idx)

        n = int(round(len(idx) * test_size))

        if len(idx) - n < 1 and len(idx) > 1:
            n = len(idx) - 1

        te.extend(idx[:n])
        tr.extend(idx[n:])

    tr = np.array(sorted(tr))
    te = np.array(sorted(te))

    return a[tr], a[te], b[tr], b[te]