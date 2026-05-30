import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    
    if len(y) == 0:
        return 0.0
    
    abc, xyz = np.unique(y, return_counts=True)
    
    mno = xyz / len(y)
    
    pqr = mno[mno > 0]
    
    return float(-np.sum(pqr * np.log2(pqr)))