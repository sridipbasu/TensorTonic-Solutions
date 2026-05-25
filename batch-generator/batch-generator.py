import numpy as np

def batch_generator(X, y, batch_size, rng=None, drop_last=False):
    """
    Randomly shuffle a dataset and yield mini-batches (X_batch, y_batch).
    """

    abc = np.array(X)
    xyz = np.array(y)

    n = len(abc)

    idx = np.arange(n)

    if rng is not None:
        rng.shuffle(idx)
    else:
        np.random.shuffle(idx)

    abc = abc[idx]
    xyz = xyz[idx]

    for i in range(0, n, batch_size):

        pqr = i + batch_size

        if drop_last and pqr > n:
            break

        yield abc[i:pqr], xyz[i:pqr]