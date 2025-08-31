+++
date = '2025-08-29T07:31:27-04:00'
draft = false
title = 'Minimal Python Package'
+++

Let's create a minimal Python package from [this tutorial](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

1. Update `pip`

```shell
python3 -m pip install --upgrade pip
```

2. Create a directory structure for your package

```raw
packaging_tutorial/
└── src/
    └── example_package_nimasarajpoor/
        ├── __init__.py
        └── example.py
```

Let's create them...

```shell
mkdir packaging_tutorial
mkdir packaging_tutorial/src
mkdir packaging_tutorial/src/example_package_nimasarajpoor
touch packaging_tutorial/src/example_package_nimasarajpoor/__init__.py
touch packaging_tutorial/src/example_package_nimasarajpoor/example.py
```

3. Inside the module `example`, we can have a simple function:

```python
def add_two(a, b):
    """
    Adds two numbers.
    """
    return a + b
```

4. Now we are going to add some extra files to make it ready for distribution.

```raw
packaging_tutorial/
├── LICENSE
├── pyproject.toml
├── README.md
├── src/
│   └── example_package_nimasarajpoor
│       ├── __init__.py
│       └── example.py
└── tests/
```

5. Choosing a build backend

Tools like `pip` and `build` do not actually convert your sources into a distribution package (like a `wheel`); that job is performed by a `build backend`. Let's have quick chat about the terms here:

* pip: The most popular tool for installing Python packages, and the one included with modern versions of Python.
* build: It is a Python package builder. It provides a CLI to build packages. It is at front-end, and it delegates the actual building to a `build backend`.
* build backend: A library that takes a source tree and builds a source distribution from it. `setuptools` is one of the common build backends.


How does build know which backend to use? It looks for a `pyproject.toml` file in the source tree, which is a standardized configuration file for Python projects. This file can specify the build backend to use, along with other metadata about the project. The `build backend` information should be provided under `[build-system]` table.
In this tutorial, the build backend `hatchling` is used. We will specify it in the `pyproject.toml` file.

6. Creating the `pyproject.toml` file

```toml
[build-system]
requires = ["hatchling >= 1.26"]
build-backend = "hatchling.build"

[project]
name = "example_package_nimasarajpoor"
version = "0.0.1"
authors = [
  { name="Example Author", email="nimasarajpoor@gmail.com" },
]
description = "A small example package"
readme = "README.md"
requires-python = ">=3.9"
classifiers = [
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]
license = "MIT"
license-files = ["LICEN[CS]E*"]

[project.urls]
Homepage = "https://github.com/NimaSarajpoor/example_package_NimaSarajpoor_repo"
Issues = "https://github.com/NimaSarajpoor/example_package_NimaSarajpoor_repo/issues"
```


Note that I've intentionally used different names for the following items:
* name of package
* name of distribution package
* name of repo

To be consistent, we can use same name. I've chosen different names to better understand the role of each item! 


7. Add simple text to `README.md` for now.

```shell

echo "This is README!" > README.md
```

8. LICENSE: <br>
To know which license is suitable for your project, you can refer to [ChooseALicense.com](https://choosealicense.com/).


9. Generating distribution archives <br>
Now it's time to generate the distribution! At front-end, we want to use `build`. so, let's make sure it is up-to-date.

```shell
python3 -m pip install --upgrade build
```

Now, at the parent directory of `pyproject.toml`, runs:
```shell
python3 -m build
```

This will create two files in the `dist/` directory.
```raw
dist/
├── example_package_nimasarajpoor-0.0.1-py3-none-any.whl
└── example_package_nimasarajpoor-0.0.1.tar.gz
```

* what is `.whl`, known as wheel file? This is `built distribution`
* what is `.tar.gz`, knonw as sdist file? This is `source distribution`


> Newer `pip` versions preferentially install built distributions, but will fall back to source distributions if needed. 


10. Uploading the distribution archives 
Now, we are in a position to upload package to `Python Package Index`. Follow these steps:

* Register an account on TestPyPI
* Create PyPI API token at https://test.pypi.org/manage/account/#api-tokens. Set the “Scope” to “Entire account”. Don’t close the page until you have copied and saved the token.

* Use twine to upload the distribution packages.

```shell
python3 -m pip install --upgrade twine
python3 -m twine upload --repository testpypi dist/*
```

You can create a github repo, and create a similar structure there. I did and I uploaded my package. You can find it here: <br> 

https://test.pypi.org/project/example-package-nimasarajpoor/0.0.1/


You can install it:

```shell
python -m pip install --index-url https://test.pypi.org/simple/ --no-deps example_package_nimasarajpoor
```

and use it as follows:

```python
from example_package_nimasarajpoor import example
example.add_two(3, 2)
```