import argparse
import mandybrot as mandy

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("real", type=float)
parser.add_argument("imag", type=float)
parser.add_argument("width", type=int)
parser.add_argument("height", type=int)
parser.add_argument("scale", type=float)
parser.add_argument("max_iters", type=int)
args = parser.parse_args()

# Sample the region
data = mandy.sample.area(
    args.real, args.imag, args.width, args.height, args.scale, args.max_iters
)

# Colour the plot
cols = mandy.colour.image(data, args.max_iters, mandy.colour.grayscale)

# Encode the image
img = mandy.colour.encode(cols)
img.save("mandy.png")
