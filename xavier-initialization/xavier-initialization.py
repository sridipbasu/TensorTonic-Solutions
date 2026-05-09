import math

def xavier_initialization(abc, xyz, pqr):
    l = math.sqrt(6 / (xyz + pqr))
    return [[j * 2 * l - l for j in i] for i in abc]