from PIL import Image
import numpy as np


def grayscale(value, max_iters):
    """
    Convert a value between zero and max_iters
    to an 8-bit grayscale colour.
    """

    x = value / max_iters * 255
    return (x, x, x)


def image(data, max_iters, colouring):
    """
    Convert data to an image using a colouring function.
    """

    height, width = data.shape
    img = np.zeros((height, width, 3), dtype=np.uint8)

    for i in range(height):
        for j in range(width):
            img[i, j] = colouring(data[i, j], max_iters)

    return img


def encode(data):
    """
    Encode an image as a PNG.
    """

    return Image.fromarray(data)
