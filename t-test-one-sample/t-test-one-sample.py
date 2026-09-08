import numpy as np

def t_test_one_sample(x: list, mu0: float) -> float:
    """
    Returns the t-statistic as a float.
    """
    x = np.array(x, dtype=float)
    abc = np.mean(x)
    xyz = np.std(x, ddof=1)

    if xyz == 0:
        if abc == mu0:
            return 0.0
        return float(np.inf) if abc > mu0 else float(-np.inf)

    return float((abc - mu0) / (xyz / np.sqrt(x.size)))