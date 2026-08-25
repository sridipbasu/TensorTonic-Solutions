import numpy as np

def streaming_minmax(D: int, batches: list, eps: float = 1e-8) -> dict:
    """
    Returns a dictionary with normalized_batches, min, and max.
    """
    abc = np.full(D, np.inf)
    xyz = np.full(D, -np.inf)
    result = []

    for batch in batches:
        batch = np.array(batch, dtype=float)
        abc = np.minimum(abc, batch.min(axis=0))
        xyz = np.maximum(xyz, batch.max(axis=0))

        denom = np.maximum(xyz - abc, eps)
        norm_batch = (batch - abc) / denom
        result.append(norm_batch)

    return {"normalized_batches": result, "min": abc, "max": xyz}