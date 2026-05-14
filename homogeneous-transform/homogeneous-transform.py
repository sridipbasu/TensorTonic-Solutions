import numpy as np

def apply_homogeneous_transform(abc, xyz):
    p = np.array(xyz, dtype=float)
    s = (p.ndim == 1)

    if s:
        p = p.reshape(1, 3)

    h = np.hstack((p, np.ones((len(p), 1))))
    r = (np.array(abc) @ h.T).T[:, :3]

    return r[0] if s else r