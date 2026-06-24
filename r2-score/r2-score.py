import numpy as np

def r2_score(y_true, y_pred) -> float:
    """
    Compute R² (coefficient of determination) for 1D regression.
    Handle the constant-target edge case:
      - return 1.0 if predictions match exactly,
      - else 0.0.
    """
    a = np.asarray(y_true, dtype=float)
    b = np.asarray(y_pred, dtype=float)

    m = np.mean(a)
    sst = np.sum((a - m) ** 2)
    sse = np.sum((a - b) ** 2)

    if sst == 0:
        return 1.0 if np.array_equal(a, b) else 0.0

    r = 1.0 - (sse / sst)
    return float(r)