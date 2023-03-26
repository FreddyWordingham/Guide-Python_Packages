import numpy as np


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


def area(real, imag, width, height, scale, max_iters):
    """
    Sample a region of the Mandelbrot set.
    """

    re = np.linspace(real - 0.5 * scale * width, real + 0.5 * scale * width, width)
    im = np.linspace(imag - 0.5 * scale * height, imag + 0.5 * scale * height, height)

    mandelbrot_set = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            mandelbrot_set[i, j] = point(re[j], im[i], max_iters)

    return mandelbrot_set
