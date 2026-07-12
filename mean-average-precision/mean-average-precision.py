import numpy as np

def mean_average_precision(y_true_list, y_score_list, k=None):
    """
    Compute Mean Average Precision (mAP) for multiple retrieval queries.
    """
    abc = []

    for x, y in zip(y_true_list, y_score_list):
        x = np.array(x)
        y = np.array(y)

        total = np.sum(x)

        if total == 0:
            abc.append(0.0)
            continue

        xyz = np.argsort(-y)
        x = x[xyz]

        if k is not None:
            x = x[:k]

        count = np.cumsum(x)
        rank = np.arange(1, len(x) + 1)

        precision = count / rank
        ap = np.sum(precision * x) / total

        abc.append(ap)

    map_value = np.mean(abc)

    return map_value, abc