def polynomial_features(values, degree):
    """
    Generate polynomial features for each value up to the given degree.
    """
    abc = []

    for x in values:
        xyz = []
        for i in range(degree + 1):
            xyz.append(x ** i)
        abc.append(xyz)

    return abc