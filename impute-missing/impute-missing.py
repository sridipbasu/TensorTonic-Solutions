import numpy as np

def impute_missing(X, strategy='mean'):
    X = np.array(X, dtype=float) 
    
    if X.ndim == 1:
        X = X.reshape(-1, 1) 
        squeeze = True
    else:
        squeeze = False
    
    result = X.copy()
    
    for col in range(X.shape[1]):
        column = X[:, col]
        valid = column[~np.isnan(column)]  
        
        if len(valid) == 0:
            fill = 0 
        elif strategy == 'mean':
            fill = np.mean(valid)
        else:
            fill = np.median(valid)
        
        result[np.isnan(column), col] = fill
    
    return result.squeeze() if squeeze else result