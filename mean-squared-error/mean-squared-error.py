import numpy as np

def mean_squared_error(y_pred, y_true):
    """
    Returns: float MSE
    """
    s = len(y_true)
    if s == 0:
        raise ValueError("Input cant be empty")
    return sum((p-t)**2 for p, t in zip(y_pred,y_true)) /s
    pass
