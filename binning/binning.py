def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    min_val = min(values)
    max_val = max(values)
    if min_val == max_val:
        return [0] * len(values)
    bin_w = (max_val-min_val) / num_bins
    result = []
    for e in values:
        bin_index = int((e - min_val) / bin_w)
        bin_index = min(bin_index, num_bins - 1)
        result.append(bin_index)
    return result