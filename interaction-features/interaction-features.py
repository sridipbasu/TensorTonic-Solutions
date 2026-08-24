def interaction_features(X: list) -> list:
    """
    Returns original features followed by unique pairwise products.
    """
    xyz = []
    for row in X:
        abc = list(row)
        d = len(row)
        for i in range(d):
            for j in range(i + 1, d):
                abc.append(row[i] * row[j])
        xyz.append(abc)
    return xyz