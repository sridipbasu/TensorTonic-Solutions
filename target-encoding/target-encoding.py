def target_encoding(abc, xyz):
    s = {}
    c = {}
    for i in range(len(abc)):
        if abc[i] not in s:
            s[abc[i]] = 0
            c[abc[i]] = 0
        s[abc[i]] += xyz[i]
        c[abc[i]] += 1
    m = {}
    for k in s:
        m[k] = s[k] / c[k]
    return [m[i] for i in abc]