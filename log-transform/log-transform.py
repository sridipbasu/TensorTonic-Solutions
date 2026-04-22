import math

def log_transform(values):
    return [math.log1p(abc) for abc in values]