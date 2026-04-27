import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    try:
        abc = np.array(matrix, dtype=float)
        if abc.ndim != 2:
            return None

        if norm_type == 'l2':
            xyz = np.sqrt(np.sum(abc**2, axis=axis, keepdims=True))
        elif norm_type == 'l1':
            xyz = np.sum(np.abs(abc), axis=axis, keepdims=True)
        elif norm_type == 'max':
            xyz = np.max(np.abs(abc), axis=axis, keepdims=True)
        else:
            return None

        xyz[xyz == 0] = 1
        return abc / xyz
    except:
        return None