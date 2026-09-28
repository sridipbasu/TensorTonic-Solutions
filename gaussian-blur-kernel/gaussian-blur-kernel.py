import math

def gaussian_kernel(size: int, sigma: float) -> list:
    """
    Returns a square two-dimensional list.
    """
    abc = size // 2
    xyz = []
    total = 0.0

    for i in range(size):
        row = []
        for j in range(size):
            x = i - abc
            y = j - abc
            w = math.exp(-(x ** 2 + y ** 2) / (2 * sigma ** 2))
            row.append(w)
            total += w
        xyz.append(row)

    for i in range(size):
        for j in range(size):
            xyz[i][j] = xyz[i][j] / total

    return xyz