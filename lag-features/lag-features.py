def lag_features(series, lags):
    """
    Create a lag feature matrix from the time series.
    """
    abc = max(lags)
    xyz = []
    for t in range(abc, len(series)):
        row = [series[t - lag] for lag in lags]
        xyz.append(row)
    return xyz