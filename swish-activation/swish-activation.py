import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    x = np.asarray(x, dtype=float)
    
    # Clip for numerical stability
    x_clipped = np.clip(x, -500, 500)
    
    # Sigmoid
    sigmoid = 1 / (1 + np.exp(-x_clipped))
    
    # Swish
    return x * sigmoid