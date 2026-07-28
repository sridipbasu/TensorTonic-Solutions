def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    abc = []
    for i in range(len(scores)):
        if i not in rated_indices:
            abc.append((scores[i], i))
    abc.sort(key=lambda x: -x[0])

    xyz = []
    for j in range(len(abc)):
        if j == k:
            break
        xyz.append(abc[j][1])
    return xyz