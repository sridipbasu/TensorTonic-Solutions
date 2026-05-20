import numpy as np
from collections import Counter
import math

def bm25_score(query_tokens, docs, k1=1.2, b=0.75):
    total = len(docs)
    if total == 0:
        return np.array([])
    tf = [Counter(d) for d in docs]
    dl = np.array([len(d) for d in docs])
    avg = np.mean(dl)
    df = Counter()
    for d in docs:
        for t in set(d):
            df[t] += 1
    out = np.zeros(total)
    for t in dict.fromkeys(query_tokens):
        dft = df.get(t, 0)
        if dft == 0:
            idf = 0
        else:
            idf = math.log((total - dft + 0.5) / (dft + 0.5) + 1)
        for pos in range(total):
            tfi = tf[pos].get(t, 0)
            bot = tfi + k1 * (1 - b + b * dl[pos] / avg)
            out[pos] += idf * (tfi * (k1 + 1)) / bot
    return out