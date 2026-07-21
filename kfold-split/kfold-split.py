import numpy as np

def kfold_split(N, k, shuffle=True, rng=None):
    """
    Returns: list of length k with tuples (train_idx, val_idx)
    """
    idx = np.arange(N)

    if shuffle:
        if rng is not None:
            idx = rng.permutation(idx)
        else:
            np.random.shuffle(idx)

    base = N // k          # minimum fold size
    extra = N % k          # first `extra` folds get one more

    out = []
    start = 0
    for i in range(k):
        size = base + (1 if i < extra else 0)
        stop = start + size

        val = idx[start:stop]
        train = np.concatenate([idx[:start], idx[stop:]])

        out.append((train.astype(int), val.astype(int)))
        start = stop

    return out