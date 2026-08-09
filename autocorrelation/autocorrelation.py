def autocorrelation(series, max_lag):
    """
    Compute the autocorrelation of a time series for lags 0 to max_lag.
    """
    abc = len(series)
    mean_val = sum(series) / abc
    xyz = sum((v - mean_val) ** 2 for v in series)

    if xyz == 0:
        return [1.0] + [0.0] * max_lag

    result = []
    for k in range(max_lag + 1):
        cov = sum((series[t] - mean_val) * (series[t + k] - mean_val) for t in range(abc - k))
        result.append(cov / xyz)
    return result