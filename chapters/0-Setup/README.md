# Project Setup

## Add pyproject.toml

Create a new `Poetry` project:

```shell
poetry init
```

-   I'm going to call this project `mandybrot`
-   Starting at version `0.1.0`
-   My description will be: `Plot the magical Mandelbrot set.`
-   I am: `FreddyWordingham <freddy@digilab.co.uk>`
-   I'm not going to add a license
-   Compatible with `Python` versions `3.8` and above
-   And I'm not going to add any dependencies right now

This will generate a [`pyproject.toml`](./pyproject.toml) file containing the project metadata.

## Add .gitignore

I'm going to add a [`.gitignore`](./.gitignore) file to my project.
Python projects use a lot of files that we don't want to commit to Git, so we can use a `.gitignore` to tell Git to ignore them.

I'm going to pull the code from https://www.toptal.com/developers/gitignore/api/python into a `.gitignore` file using the `curl` command:

```shell
curl -L https://www.toptal.com/developers/gitignore/api/python > .gitignore
```

Alternatively, you can go to [gitignore.io](https://gitignore.io/) and generate a template more tailored to your needs.

## Add Library

I'm going to add a mandybrot directory to my project.
This will contain the code for my Python package.

For now, I'm just going to add a [`__init__.py`](./mandybrot/__init__.py) file to the directory.
This is an empty file that tells Python that this directory is a package.

```shell
mkdir mandybrot
touch mandybrot/__init__.py
```

## Poetry Install

Now I'm ready to install my project with Poetry:

```shell
poetry install
```

This will install the project dependencies into a virtual environment.

Note that a file called `poetry.lock` has been created.
This file contains the exact versions of the dependencies that were installed.
This is important because it means that if I share my project with someone else, they will install the same versions of the dependencies that I did.

If I delete the `poetry.lock` file, and then run `poetry install` again, it will install the latest versions of the dependencies.
This is useful if I want to update my dependencies to the latest versions, or if I want to install a new dependency that is conflicting with an existing one specified by the more restrictive `poetry.lock` file.

## Poetry Run

When we run a Python script we want to run it within the virtual environment that Poetry just created for us.

You can do this by running `poetry run` before the command you want to run:

```shell
poetry run python path/to/my_script.py
```

The `-c` option lets us run a single command:

```shell
poetry run python -c "print('Hello World')"
```

You can test if everything is working by running `import mandybrot`:

```shell
poetry run python -c "import mandybrot"
```

(Nothing should happen, but if you get an error then something is wrong.)
Your files should look identical to the files in this directory.

## Return

[Return to the top-level README](./../../README.md)
