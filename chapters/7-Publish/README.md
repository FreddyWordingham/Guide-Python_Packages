# Publish

Finally, let's be brave and publish our package to PyPI.
There's no good reason for you not to do this, as it's free and easy to do, and it's an awesome thing to be able to say you've done!

## Create or log in to PyPI

Next, we need to create an account on PyPI, or log in if we already have one.
You can do this at [https://pypi.org/account/register/](https://pypi.org/account/register/).

## Create an API token

Go to [https://pypi.org/manage/account/token/](https://pypi.org/manage/account/token/) and create a new API token.
Make sure to copy the token somewhere safe, as you won't be able to see it again.

## Add the token to Poetry

```bash
poetry config pypi-token.pypi your-token-you-just-created
```

## Build

Now we need to build the package.

```bash
poetry build
```

## Publish

Run the following command to publish the package to PyPI:

```bash
poetry publish
```

---

**Note**

The name you give your package must be unique on PyPI.
If you try to publish a package with a name that already exists, you'll get an error.

---

## Install

In another project, we can now install `mandybrot` like any other package!

```toml
[tool.poetry.dependencies]
mandybrot = "^0.1.0"
```

## Return

[Return to the top-level README](./../../README.md)
