def frequency_encoding(abc):
    d = {}
    n = len(abc)

    for i in abc:
        if i not in d:
            d[i] = 0
        d[i] += 1

    return [d[i] / n for i in abc]