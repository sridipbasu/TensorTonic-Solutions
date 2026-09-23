import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    x = np.array(x, dtype=float)
    abc = np.var(x, ddof=1)
    xyz = np.sqrt(abc)

    return {"variance": float(abc), "standard_deviation": float(xyz)}