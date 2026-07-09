def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    abc = recommended[:k]
    xyz = set(relevant)

    count = 0

    for i in abc:
        if i in xyz:
            count += 1

    precision = count / k
    recall = count / len(relevant)

    return [precision, recall]