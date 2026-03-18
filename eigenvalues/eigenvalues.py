import numpy as np

def calculate_eigenvalues(matrix):
    """
    Calculate eigenvalues of a square matrix.
    """
    try:
        matrix = np.asarray(matrix, dtype=object)
    except (ValueError, TypeError):
        return None
    if matrix.ndim != 2:
        return None
    if matrix.shape[0] == 0 or matrix.shape[1] == 0:
        return None
    if matrix.shape[0] != matrix.shape[1]:
        return None

    try:
        matrix = matrix.astype(float)
    except (ValueError, TypeError):
        return None
    eigenvalues = np.linalg.eigvals(matrix)
    index_sort = np.lexsort((eigenvalues.imag, eigenvalues.real))
    return eigenvalues[index_sort]