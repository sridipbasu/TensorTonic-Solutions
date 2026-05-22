import numpy as np

def triplet_loss(anchor, positive, negative, margin=1.0):
    """
    Compute Triplet Loss for embedding ranking.
    """

    abc = np.array(anchor)
    xyz = np.array(positive)
    pqr = np.array(negative)

    if abc.ndim == 1:
        abc = abc.reshape(1, -1)
        xyz = xyz.reshape(1, -1)
        pqr = pqr.reshape(1, -1)

    ap = np.sum((abc - xyz) ** 2, axis=1)
    an = np.sum((abc - pqr) ** 2, axis=1)

    # Triplet loss
    loss = np.maximum(0, ap - an + margin)

    # Mean loss
    return np.mean(loss)