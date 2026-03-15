import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    A = np.array(A)

    if A.shape[0] != A.shape[1]:
        return 'Matrix has to Square matrix!'
    sum = 0
    for i in range(len(A)):
        sum = sum + A[i][i]
    return sum
    pass
