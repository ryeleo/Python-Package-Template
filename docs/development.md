This document discusses setting up local development for this project on your own personal Linux box.

> We use Ubuntu 20.04 (ex. Windows Subsystem for Linux) as our development environment.
>
> We use VS Code as our editor.
>
> We use [Python Hatch](https://hatch.pypa.io/latest/) for this project.

## Prerequisites

### Python 3.8

Install python 3.8.

    sudo apt-get install python3.8 python3.8-venv

It is wise to update pip at this time.

    python3.8 -m pip install --upgrade pip

### Hatch

We use Hatch to manage our development environment (and build process).

> What is Hatch? "Hatch is a modern, extensible Python project manager."

You can easily [install Hatch](https://hatch.pypa.io/latest/install/) using pip.

    pip install hatch

We advise running the following command once you've installed Hatch.
This will ensure virtual environments exist within the Hatch project's directory.

> This makes integrating with VSCode and other IDEs simpler.

    hatch config set dirs.env.virtual ./venv

## Getting Started

Once you have [installed Hatch](#hatch), we can jump right into our development environment using the following command.

    hatch shell

At this point, running `pip freeze` should reveal that all dependencies are installed for you!

> In fact, you can grep for "-e " to ensure that this package is correctly installed in editable mode. 
>```bash
> pip freeze | grep "-e "
>```

### Any Issues?

A great place to start if there are issues with Getting Started, is to run `hatch env prune`. 
This will remove all Hatch-managed and restart fresh.

> ⚠ This will fail if any shells are using any of your hatch-managed venv(s).
>
> ℹ Either `deactivate` or `exit` any currently opened shells that are using your hatch-managed venv(s).

## Dependency Management

We use "pyproject.toml" to define all dependencies for development and production.

### Production Dependencies

In `[project]`, there is the **minimum** list of packages required for installation: `dependencies`.
This list should follow best practices, I.e.,

1. do **NOT** pin specific versions, and 
2. do **NOT** specify sub-dependencies.

### Development Dependencies 

Hatch provides features to manage Development dependencies as well!
Within "hatch.toml" there is the `[envs.default]` section


## Automated Testing

Pytest is used to automatically test this project.
All tests are contained in the "tests" directory.

To run all the automated tests for this project, you can simply, "`run` the `coveragee` script provided by our Hatch `default` environment," i.e.: `hatch run coveragee`

> ℹ Review "hatch.toml" in this project's root to learn what other scripts are available!
>
> ℹ Learn more by reading ["Hatch Environments Scripts" documentation](https://hatch.pypa.io/latest/environment/#scripts).

    hatch run coveragee
    ===================== test session starts =====================
    platform linux -- Python 3.x.y, pytest-6.x.y, py-1.x.y, pluggy-1.x.y
    cachedir: $PYTHON_PREFIX/.pytest_cache
    ... omitted for brevity...
