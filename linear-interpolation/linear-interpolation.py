def linear_interpolation(abc):
    x = abc[:]
    n = len(x)

    i = 0

    while i < n:
        if x[i] is None:
            l = i - 1
            r = i

            while x[r] is None:
                r += 1

            for j in range(i, r):
                x[j] = x[l] + ((j - l) / (r - l)) * (x[r] - x[l])

            i = r

        else:
            i += 1

    return x