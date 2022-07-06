# Python Project Template 0.1.0

Python projects are much easier to use and maintain if we standardize around the following:

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

To get started using this project structure for your own project, here are the initial steps:

> Further instructions are provided in "TODO: setup your..." sections below.

1. Rename the `examplepkg` directory in the `src/` directory.
    * For **public** projects, we try to follow PEP8 convention: "Python packages should have short, all-lowercase names... the use of underscores is discouraged."
    * For **private** projects, underscores *should* be used in the name if it improves readability (or if it makes naming easier)!
2. Delete (or rename) `hello_world.py` and `test_hello_world.py`
3. Replace this `README.md` with `README.md.template`.
    * You can continue to reference *this* (meta) README.md in our SCM server: https://git.uoregon.edu/projects/ISN/repos/python-project-structure/browse



# Dependency Management

Dependency management is covered in our [Developer docs](docs/development.md).

## TODO: Setup Dependencies

> ℹ See [Developer docs](docs/development.md) that discuss Dependency management in depth.

1. Ensure that production and development dependencies are sufficient but not too restrictive.
    * E.g., double check that 'best practices' are followed, as outlined in the [Developer docs](docs/development.md).

> ⚠ When [Hatch gains support for lock files](https://github.com/pypa/hatch/discussions/226#discussioncomment-2714692), we will update this process to include using a lock file for maximum (CICD) stability.

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
2. Update the `name` of the package, **replacing underscores with hyphens.**
    * **NOTICE: We do NOT use underscores (and only use hyphens)** for the setup.py `name` in Python. 
    * This convention is against PEP8... So, why do this? This is for practical use of setuptools + pip: underscores are actually incompatible with setuptools when using our pypi.uoregon.edu server. See [(somewhat) relevant stack overflow answer](https://stackoverflow.com/a/19131777/1227086)
2. Finally, search in [`setup.py`](setup.py) for any remaining "TODO"s.
    * E.g., name, description, keywords, classifiers.



# Automatic Testing

The basics of automatic testing with pytest is discussed at the end of our [developer guide (`docs/development.md`)](docs/development.md).



# Continuous Integration and Deployment

We use a Jenkins Shared Library to provide a single command to enable CICD for any python project on our BitBucket server.

## Initial, One-Time Setup Steps

There are a couple of pieces that we need to establish before CICD will work for your new python project.
These include updating your project's Jenkinsfile, and updating Bitbucket to trigger your Jenkins job.
In short, you will have to do the following, discussed in detail below:

1. Configure Jenkinsfile (choose a Python Package Index).
2. Set up "Parameterized Build for Jenkins" hook in your Bitbucket repo.

> Our Jenkins server will automatically create a pipeline for any repo in the [ISN project](https://git.uoregon.edu/projects/ISN), via a Jenkins Organization Folder.

### Jenkinsfile: Which Python Package Index?

> If using pypi.uoregon.edu, there are some [additional one-time setup instructions for your package (internal docs)](https://confluence.uoregon.edu/display/NTS/Deploy+to+pypi.uoregon.edu)

You must decide whether you will be publishing to pypi.org or our private pypi.uoregon.edu server.

1. Simply update the `packageIndex` in [your Jenkinsfile](../Jenkinsfile). Choose from:
    * 'pypi.org' or, 
    * 'pypi.uoregon.edu'

> See all current options for 'buildPythonProject' (and default values) at [defaultPythonProjectConfig.groovy](https://git.uoregon.edu/projects/ISN/repos/ntsjenkins_shared_library/browse/vars/defaultPythonProjectConfig.groovy)

### Bitbucket Webhook

Our default settings and how to enable them is well discussed in our [internal documentation](https://confluence.uoregon.edu/pages/viewpage.action?pageId=458892621#NTSJenkinsBitbucketIntegration-EnableDefaultSettingsformyrepo).

In short, these are the steps to enable the Bitbucket Webhook in our ISN project:

1. Navigate to your "Repository Settings → Hooks"
2. Change from 'Inherited (disabled)' to "Enabled" for Parametrized build for Jenkins.
3. Update the 'Job Name' to align with the Jenkins Job URL.
