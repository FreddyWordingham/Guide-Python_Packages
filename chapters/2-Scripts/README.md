# Scripts

## Add run.py

Our package will be a command line tool, so we'll need a way to run it.
Create a directory called [`scripts`](./scripts):

```shell
mkdir scripts
```

And then within this directory, create a file called [`run.py`](./scripts/run.py):

```shell
touch scripts/run.py
```

## Add run function

Inside `run.py` we'll add some code to parse the command line arguments, and then call our `point()` function:

```python
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
```

## Try it

We can run the script by running the following command:

```shell
poetry run python scripts/run.py 0 0 100
```

The first argument is the path to the script, and the remaining arguments are the values for `real` and `imag`.

This should print out the following:

```shell
(0.0, 0.0) -> 100
```

## Return

[Return to the top-level README](./../../README.md)
