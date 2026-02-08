def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    n = len(X)
    d_in = len(X[0])
    d_out = len(W[0])

    Y =[]
    for i in range(n):
        row =[]
        for j in range(d_out):
            total = 0.0
            for k in range(d_in):
                total = total + X[i][k] * W[k][j]
            total = total + b[j]
            row.append(total)
        Y.append(row)
    return Y