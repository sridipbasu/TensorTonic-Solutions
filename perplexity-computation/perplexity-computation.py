import math

def perplexity(abc, xyz):
    s = 0
    n = len(xyz)
    for i in range(n):
        s += math.log(abc[i][xyz[i]])
    return math.exp(-s / n)