import numpy as np

def softmax(z):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    a = np.array(z)
    
    if a.ndim == 1:
        shift = a - np.max(a)
        boom = np.exp(shift)
        return boom / np.sum(boom)
    
    elif a.ndim == 2:
        shift = a - np.max(a, axis=1, keepdims=True)
        boom = np.exp(shift)
        return boom / np.sum(boom, axis=1, keepdims=True)
    pass