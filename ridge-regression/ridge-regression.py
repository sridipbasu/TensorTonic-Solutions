def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    x = np.array(X)
    y = np.array(y)

    xtx = x.T @ x

    d = xtx.shape[0]
    i = np.eye(d)

    r_mat = xtx +lam * i
    inv = np.linalg.inv(r_mat)
    xty = x.T @ y
    w = inv @ xty
    return w.tolist()