def mean_rating_imputation(ratings_matrix, mode):
    """
    Fill missing ratings (zeros) with user or item means.
    """
    abc = [row[:] for row in ratings_matrix]

    if mode == "user":
        for i in range(len(abc)):
            xyz = [v for v in abc[i] if v != 0]
            mean_val = sum(xyz) / len(xyz) if xyz else 0

            for j in range(len(abc[i])):
                if abc[i][j] == 0:
                    abc[i][j] = mean_val

    elif mode == "item":
        rows = len(abc)
        cols = len(abc[0])

        for j in range(cols):
            xyz = []
            for i in range(rows):
                if abc[i][j] != 0:
                    xyz.append(abc[i][j])

            mean_val = sum(xyz) / len(xyz) if xyz else 0

            for i in range(rows):
                if abc[i][j] == 0:
                    abc[i][j] = mean_val

    return abc