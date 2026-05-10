import numpy as np
from collections import Counter

def mean_median_mode(abc):
    x = np.array(abc)
    d = Counter(x)
    m = max(d.values())
    z = min(i for i in d if d[i] == m)

    return (
        float(np.mean(x)),
        float(np.median(x)),
        float(z)
    )