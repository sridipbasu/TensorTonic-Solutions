import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    a = np.array(a)
    b = np.array(b)

    n_a = np.linalg.norm(a)
    n_b = np.linalg.norm(b)

    if n_a == 0 or n_b == 0:
        return 0
    return np.dot(a,b) / ((n_a*n_b))
    pass