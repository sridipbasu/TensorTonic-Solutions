import math

def cyclic_encoding(values, period):
    """
    Encode cyclic features as sin/cos pairs.
    """
    xyz = []
    for v in values:
        theta = 2 * math.pi * v / period
        xyz.append([math.sin(theta), math.cos(theta)])
    return xyz