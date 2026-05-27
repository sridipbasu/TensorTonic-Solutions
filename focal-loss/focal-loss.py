import numpy as np

def focal_loss(p, y, gamma=2.0):
    abc = np.clip(np.array(p, dtype=float), 1e-15, 1 - 1e-15)
    xyz = np.array(y, dtype=float)
    qrs = -((1 - abc)**gamma * xyz * np.log(abc) + abc**gamma * (1 - xyz) * np.log(1 - abc))
    return np.mean(qrs)