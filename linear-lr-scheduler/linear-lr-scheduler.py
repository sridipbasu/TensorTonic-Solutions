def linear_lr(a, b, c, d=0.0, e=0):
    if a < e:
        return (a * c) / e if e > 0 else c
    if a <= b:
        return d + (c - d) * (b - a) / (b - e) if b > e else d
    return d