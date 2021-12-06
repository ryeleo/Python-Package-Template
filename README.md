Python projects must have some standard structure if we want to standardize around the following:

* Dependency Management.
* Technical Documentation Management (via MkDocs).
* Packaging (via setuptools).
    * Exposing CLI Tools (via 'Command Line Scripts').
* Automatic Testing (via pytest).
* Continuous Integration and Deployment (via Jenkins).

This repository is a starting point for any python project!
You should clone this project and make updates as indicated below.

Before jumping into details and instructions, it is worth reviewing our project structure in the file system.

      project_template
      ├── docs
      │   ├── index.md
      │   ├── development.md
      │   ├── release-notes.md
      │   └── user-guide.md
      ├── MANIFEST.in
      ├── mkdocs.yml
      ├── README.md
      ├── setup.py
      ├── src
      │   └── examplepkg
      │       ├── hello_world.py
      │       └── __init__.py
      └── tests
          └── test_hello_world.py

The project structure can be conceptually split into three chunks:

1. The first several files are part of  project documentation:

        ├── docs
        │   ├── index.md
        │   ├── development.md
        │   ├── release-notes.md
        │   └── user-guide.md
        ├── MANIFEST.in
        ├── mkdocs.yml
        ├── README.md

2. Then there is the production code:

        ├── setup.py
        ├── src
        │   └── examplepkg
        │       ├── hello_world.py
        │       └── __init__.py

3. And finally, the test code:

        └── tests
            └── test_hello_world.py

# Getting Started

> If you have not used this project structure, I recommend getting the `examplepkg` up and running.
> Read through [`docs/development.md`](docs/development.md) to get `examplepkg` installed -- including the `hello` command-line tool!

To get started using this project sturcture for your own project, here are the initial steps:

> Further instructions are provided in "TODO: setup your..." sections below.

1. Rename the `examplepkg` directory in the `src/` directory.
    * For **public** projects, we try to follow PEP8 convention: "Python packages should also have short, all-lowercase names, although the use of underscores is discouraged."
    * For **private** projects, underscores *should* be used in the name if it improves readability.
2. Delete (or rename) `hello_world.py` and `test_hello_world.py`
3. Replace this `README.md` with `README.md.template`.
    * You can continue to reference *this* (meta) README.md in our SCM server: https://git.uoregon.edu/projects/ISN/repos/python_project_structure/browse




# Dependency Managment

Dependency management is performed in two places.
There is a `setup.py` file and the `requirements.txt` file.

> The former is discussed more in the Packaging section below.

Dependency management is well discussed in our [developer guide (`docs/development.md`)](docs/development.md).

## TODO: setup your requirments.txt

Dependency management using Python Virtual Environments is the best way to go!

1. Creat a Python Virtual Environment in your project, and activate it (`venv/`)

        python3 -m venv venv
        source venv/bin/activate

2. Now that the venv is active, install your development-dependencies using `pip`. 
For example, you will want to install our standard development dependencies: `flake8` and `pytest`.

        pip install flake8 pytest

3. Finally, run `pip freeze > requirements.txt` to lock **all** the package versions in this project.

        pip freeze > requirments.txt

The produced `requirements.txt` file captures all of the packages that are required to support your dependencies!

## TODO: setup your setup.py install_requires

In `setup.py`, there is the **minimum** List of packages required for installation: `install_requires`.
This list should follow best practices, I.e.,

1. do **NOT** pin specific versions, and 
2. do **NOT** specify sub-dependencies.

Assuming your project depends on the `netdot` and `requests` packages, you're  `install_requires` list will look something like the following:

    install_requires=[
        "netdot>=0.1", 
        "requests>=2.0"
    ]

> This list should only include dependencies that production code depends on.
> E.g., `pytest` and `flake8` should *never* be part of `install_requires`.



# Documentation Management

We use [MkDocs](https://www.mkdocs.org/) to manage project documentation.
There are several pieces of documentation to review

    ├── docs
    │   ├── index.md
    │   ├── development.md
    │   ├── release-notes.md
    │   └── user-guide.md
    ├── MANIFEST.in
    ├── mkdocs.yml
    ├── README.md

> The `docs/` directory is perfectly readable as Markdown without even installing MkDocs!
> E.g., It works perfectly well when viewed on your SCM server, in VSCode, as well as other 'Markdown Rendering' tools!

* `docs/` contains documentation for the entire project.
* `MANIFEST.in` exists to ensure that setuptools packaging process include the `docs/` directory.
* `mkdocs.yml` is a MkDocs configuration file, used to 'serve' the `docs/` directory using MkDocs (discussed in [`docs/README.md`](docs/README.md)).
* `README.md` is just a pointer to `docs/README.md` (see [`README.md.template`](README.md.template)).

## TODO: setup your documentation

1. Provide your project's name in `mkdocs.yml`
2. Search through the `docs` directory for "TODO"s.



# Packaging

Packaging is all done via setuptools, as dictated by [`setup.py`](setup.py).

## TODO: setup your setup.py details and entry_points

1. If you want to expose any command-line tools from your package, update `entry_points`.
2. Finally, search in [`setup.py`](setup.py) for any remaining "TODO"s.
    * E.g., name, description, keywords, classifiers.



# Automatic Testing

The basics of automatic testing with pytest is discussed at the end of our [developer guide (`docs/development.md`)](docs/development.md).



# Continuous Integration and Deployment

TODO

TODO: Setup a default pipeline in ntsjenkins to enable building this project with a VERY simple Jenkinsfile.
The only parameter in the Jenkinsfile should be 'pythonPackageIndex' -- to allow users to select between pypi.uoregon.edu (private) and pypi.org (public).
