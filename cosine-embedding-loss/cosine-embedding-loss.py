import math
def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    """
    dot = sum(x*y for x, y in zip(x1,x2))
    n1 = math.sqrt(sum(x*x for x in x1))
    n2 = math.sqrt(sum(y*y for y in x2))
    c_sim = dot /(n1*n2)
    if label ==1:
        return 1-c_sim
    else:
        return max(0.0,c_sim-margin)