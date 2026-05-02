def text_chunking(abc, xyz, pqr):
    res = []
    step = xyz - pqr
    for i in range(0, len(abc), step):
        chunk = abc[i:i+xyz]
        res.append(chunk)
        if i + xyz >= len(abc):
            break
    return res