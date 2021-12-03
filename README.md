# Overview

Python projects must have some standard structure if we want to standardize around the following:

* Dependency Management.
* Technical Documentation Management (via MkDocs).
* Packaging (via setuptools).
* Exposing CLI Tools (via 'Command Line Scripts').
* Automatic Testing (via pytest).
* Continuous Integration and Deployment (via Jenkins).

This repository is a starting point for any python project!

> This `README.md` file should be replaced with `README.md.template` in *your* project repo!

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

## Getting Started

> If you have not used this project structure, I recommend getting the `examplepkg` up and running.
> Read through [`docs/development.md`](docs/development.md) to get `examplepkg` installed -- including the `hello` command-line tool!

To get started using this project sturcture for your own project, here are the initial steps:

> Further instructions are provided in "TODO: setup your..." sections below.

1. Rename the `examplepkg` directory in the `src/` directory.
    * For **public** projects, we try to follow PEP8 convention: "Python packages should also have short, all-lowercase names, although the use of underscores is discouraged."
    * For **private** projects, underscores *should* be used in the name if it improves readability.
2. Delete (or rename) `hello_world.py` and `test_hello_world.py`



## Dependency Managment

Dependency management is performed in two places.
There is a `setup.py` file and the `requirements.txt` file.

Dependency management is well discussed in our [developer guide (`docs/development.md`)](docs/development.md).

### TODO: setup your requirments.txt

Dependency management using Python Virtual Environments is the best way to go!

1. Creat a Python Virtual Environment in your project, and activate it (`venv/`)

       python3 -m venv venv
       source venv/bin/activate

2. Now that the venv is active, install dependencies using `pip`. 
For example, you may depend on the popular [`requests` package](https://pypi.org/project/requests/).

      pip install requests

3. Finally, run `pip freeze > requirements.txt` to lock **all** the package versions in this project.

      pip freeze > requirments.txt

The produced `requirements.txt` file captures all of the packages that are required to support your dependencies!

### TODO: setup your setup.py

In `setup.py`, there is the **minimum** List of packages required for installation: `install_requires`.
This list should follow best practices, I.e.,

1. do **NOT** pin specific versions, and 
2. do **NOT** specify sub-dependencies.



## Documentation Management

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

> The `docs/` directory is perfectly readable as Markdown without even installing MkDocs.

* `README.md` is just a pointer to `docs/README.md` (see `README.md.template`).
* `docs/` contains documentation for the entire project.
* `mkdocs.yml` is a MkDocs configuration file, used to 'serve' the `docs/` directory using MkDocs (discussed in `docs/README.md`).
* `MANIFEST.in` exists to ensure that setuptools packaging process include the `docs/` directory.

### TODO: setup your documentation

1. Provide your project's name in `mkdocs.yml`
2. Search through the `docs` directory for "TODO"s.



## Packaging

TODO: discuss setup.py



## Exposing CLI tools

TODO



## Automatic Testing

TODO



## Continuous Integration and Deployment

TODO

TODO: Setup a default pipeline in ntsjenkins to enable building this project with a VERY simple Jenkinsfile.
The only parameter in the Jenkinsfile should be 'pythonPackageIndex' -- to allow users to select between pypi.uoregon.edu (private) and pypi.org (public).
