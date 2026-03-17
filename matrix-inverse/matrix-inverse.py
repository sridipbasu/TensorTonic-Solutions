import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    A = np.array(A)
    if A.ndim !=2:
        return None

    row,col = A.shape
    if row != col:
        return None

    det = np.linalg.det(A)
    if abs(det) < 1e-10:
        return None

    return np.linalg.inv(A)
    '''
    ndim checks if the input is 2D array
    A.shape checks if its a square matrix
    next det checks if det = 0 then no inverse
    finally computes and returns the inverse of the matrix A
    '''
    pass
    
