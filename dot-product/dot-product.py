import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """
    x = np.array(x)
    y = np.array(y)
    
    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("1D array input only")
    
    if x.shape[0] != y.shape[0]:
        raise ValueError("Arrays should have same len")
    
    return float(np.dot(x, y))