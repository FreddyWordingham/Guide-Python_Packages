def point(real, imag, max_iters):
    """
    Determine the number of iterations required to escape a
    circle of radius 2.0 from a given initial complex point.
    """

    c = real + imag * 1j

    z = 0j
    for i in range(max_iters):
        z = z * z + c

        if abs(z) > 2.0:
            return i

    return max_iters
