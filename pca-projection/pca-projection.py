import numpy as np

def pca_projection(X, k):
    abc = np.array(X, dtype=float)
    n, d = abc.shape
    
    m = np.mean(abc, axis=0)
    c = abc - m
    
    cov = np.dot(c.T, c) / (n - 1)
    
    val, vec = np.linalg.eigh(cov)
    
    idx = np.argsort(val)[::-1]
    w = vec[:, idx[:k]]
    
    res = np.dot(c, w)
    
    return res.tolist()