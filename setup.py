from setuptools import setup, find_packages
import os


# From https://packaging.python.org/guides/single-sourcing-package-version/#single-sourcing-the-package-version
def read_project_file(relative_file_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, relative_file_path), 'r') as file_pointer:
        return file_pointer.read()


setup(
    name="examplepkg", # TODO: Update to match your package directory's name
    version='0.1.0',  # Try to follow 'semantic versioning', i.e. https://semver.org/ 
    description="TODO", # TODO: Fill-in a *short* description
    long_description_content_type='text/markdown',
    long_description=read_project_file('docs/user-guide.md'),
    include_package_data=True,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    license='MIT',
    author='University of Oregon',
    author_email='ntsjenkins@uoregon.edu',
    keywords=['NTS', 'UO'], # Provide ANY additional keywords that you want to!
    entry_points={ # TODO: Fill-in console_scripts -- remove if you have no CLI.
        'console_scripts': [
            'hello=examplepkg.hello_world:main'
            # Place `hello` command in PATH: enables running `hello` as a command-line interface tool.
        ]
    },
    install_requires=[
        # TODO: List of the MINIMUM set of packages -- remove if you only require the Python stdlib!
        # I.e., (1) do NOT pin specific versions, and 
        #       (2) do NOT specify sub-dependencies.
    ],
    classifiers=[  # TODO: Classifiers selected from https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers', 
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)