import numpy as np

def roc_curve(y_true, y_score):
    """
    Compute ROC curve from binary labels and scores.
    """
    y_true = np.array(y_true)
    y_score = np.array(y_score)

    abc = np.argsort(-y_score)
    y1 = y_true[abc]
    y2 = y_score[abc]

    tp = np.cumsum(y1 == 1)
    fp = np.cumsum(y1 == 0)

    xyz = np.where(np.diff(y2))[0]
    xyz = np.r_[xyz, len(y2) - 1]

    tp = tp[xyz]
    fp = fp[xyz]

    p = np.sum(y_true == 1)
    n = np.sum(y_true == 0)

    tpr = tp / p
    fpr = fp / n

    tpr = np.r_[0, tpr]
    fpr = np.r_[0, fpr]
    thresholds = np.r_[np.inf, y2[xyz]]

    return fpr, tpr, thresholds