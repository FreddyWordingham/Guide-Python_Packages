# Images

So far we have a function that can calculate the number of iterations for a given point.
We can use this to create an image by looping over an array of points, calculating the number of iterations for each point and then turning those iterations into a colour.

## Numbers to RGB

We can create an image by converting each of these numbers into a colour encoded by a tuple of three numbers representing the red, green and blue components.
Each of these components can be any number between 0 and 255, and we can use these numbers to create a wide range of colours.

Let's create a new file called [`colour.py`](./mandybrot/colour.py) next to `sample.py`:

```shell
touch mandybrot/colour.py
```

And then link it to the library by adding an import to the [`__init__.py`](./mandybrot/__init__.py) file:

```python
from . import colour
```

## Grayscale "colouring"

Back inside [`colour.py`](./mandybrot/colour.py) we'll add a function called `grayscale()` which will convert an integer number into an RGB colour:

```python
def grayscale(value, max_iters):
    """
    Convert a value between zero and max_iters
    to an 8-bit grayscale colour.
    """

    x = value / max_iters * 255
    return (x, x, x)
```

(Yeah, I know, it's not really a colour, but it's a good starting point - and we'll add more colouring functions later.)

## Image data

We now have a method of generating an array of numbers, and a function to turn each of them into an RGB colour.

Next let's add a function named `image()` to the bottom of the `colour.py` file, which takes an array of numbers and a colouring function and returns an array of RGB colours:

```python
import numpy as np # We can add this to the top of the for neatness.

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
```

## Encoding a PNG image

Finally, we need a way to store the image array into a PNG image.
We can do this using the `PIL` (Python Imaging Library) library:

```shell
poetry add pillow
```

And then we'll add a function called `encode()` to the bottom of the `colour.py` file:

```python
from PIL import Image # We can add this to the top of the for neatness.

def encode(data):
    """
    Encode an image as a PNG.
    """

    return Image.fromarray(data)
```

## Putting it all together

We can now put all of these functions together to create an image of the Mandelbrot set.
We'll replace the [`run.py`](./scripts/run.py) file with the following code:

```python
import argparse
import os

import mandybrot as mandy

OUTPUT_DIR = "output"

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("real", type=float)
parser.add_argument("imag", type=float)
parser.add_argument("width", type=int)
parser.add_argument("height", type=int)
parser.add_argument("scale", type=float)
parser.add_argument("max_iters", type=int)
args = parser.parse_args()

# Create output directory
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Sample the region
data = mandy.sample.area(
    args.real, args.imag, args.width, args.height, args.scale, args.max_iters
)

# Colour the plot
cols = mandy.colour.image(data, args.max_iters, mandy.colour.grayscale)

# Encode the image
img = mandy.colour.encode(cols)
img.save(os.path.join(OUTPUT_DIR, "mandy.png"))
```

## Try it

We can now run the script to create an image of the Mandelbrot set:

```shell
poetry run python scripts/run.py -0.5 0 1000 500 0.0025 100
```

You should see a file called `mandy.png` in the `output/` directory.
If you open it you should see something like this:

![Mandelbrot set](./output/mandy.png)

## Return

[Return to the top-level README](./../../README.md)
