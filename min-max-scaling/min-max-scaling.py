def min_max_scaling(data):
    """
    Scale each column of the data matrix to the [0, 1] range.
    """

    rows = len(data)
    cols = len(data[0])

    abc = [[0.0 for _ in range(cols)] for _ in range(rows)]

    for j in range(cols):

        xyz = [data[i][j] for i in range(rows)]

        mn = min(xyz)
        mx = max(xyz)

        rng = mx - mn

        for i in range(rows):

            if rng == 0:
                abc[i][j] = 0.0
            else:
                abc[i][j] = (data[i][j] - mn) / rng

    return abc