import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.array(A)
    row,col=A.shape
    transpose_matrix = np.zeros((col,row), dtype=A.dtype)

    for i in range(row):
        for j in range(col):
            transpose_matrix[j,i] = A[i,j]
    return transpose_matrix
    pass
