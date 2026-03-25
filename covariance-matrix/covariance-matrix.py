import numpy as np

def covariance_matrix(x):
    """
    Compute covariance matrix from dataset X.
    """
    x = np.array(x)
    if x.ndim !=2:
        return None
    n,d = x.shape
    if n<2:
        return None
    mew= np.mean(x, axis=0)
    x_cen = x-mew
    cov = (x_cen.T @x_cen) / (n-1)
    return cov
    pass