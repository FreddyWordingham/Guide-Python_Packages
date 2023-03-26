import argparse
import mandybrot as mandy

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("real", type=float)
parser.add_argument("imag", type=float)
parser.add_argument("max_iters", type=int)
args = parser.parse_args()

# Sample the point
iterations = mandy.sample.point(args.real, args.imag, args.max_iters)

# Print the result
print(f"({args.real}, {args.imag}) -> {iterations}")
