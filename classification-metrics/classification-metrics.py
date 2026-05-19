import numpy as np

def classification_metrics(y_true, y_pred, average="micro", pos_label=1):
    a = np.array(y_true)
    b = np.array(y_pred)

    c = np.unique(np.concatenate((a, b)))

    p = []
    r = []
    f = []
    s = []

    for i in c:
        tp = np.sum((a == i) & (b == i))
        fp = np.sum((a != i) & (b == i))
        fn = np.sum((a == i) & (b != i))

        pr = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rc = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * pr * rc) / (pr + rc) if (pr + rc) > 0 else 0.0

        p.append(pr)
        r.append(rc)
        f.append(f1)
        s.append(np.sum(a == i))

    acc = float(np.mean(a == b))

    if average == "micro":
        tp = np.sum(a == b)
        fp = np.sum(a != b)
        fn = fp

        pr = tp / (tp + fp) if (tp + fp) > 0 else 0.0
        rc = tp / (tp + fn) if (tp + fn) > 0 else 0.0
        f1 = (2 * pr * rc) / (pr + rc) if (pr + rc) > 0 else 0.0

    elif average == "macro":
        pr = np.mean(p)
        rc = np.mean(r)
        f1 = np.mean(f)

    elif average == "weighted":
        pr = np.average(p, weights=s)
        rc = np.average(r, weights=s)
        f1 = np.average(f, weights=s)

    elif average == "binary":
        i = list(c).index(pos_label)
        pr = p[i]
        rc = r[i]
        f1 = f[i]

    return {
        "accuracy": float(acc),
        "precision": float(pr),
        "recall": float(rc),
        "f1": float(f1)
    }