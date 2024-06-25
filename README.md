# Python-pyls

Create pyproject.toml:

Create a pyproject.toml file in your project directory with the following content:

toml
Copy code
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[tool.pyls.scripts]
pyls = "script:main"
This configuration sets up setuptools as the build backend and defines a script entry point for pyls.



Create setup.py:

Create a setup.py file in the same directory as pyproject.toml:

python
Copy code
from setuptools import setup

setup(
    name='pyls',
    version='0.1',
    py_modules=['script'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        pyls=script:main
    ''',
)
Install the Package:

Now, you can install your script as a package using pip:

bash
Copy code
pip install .
Run pyls Command:

After installation, you can run your script using the pyls command:

bash
Copy code
pyls
This will execute your script.py file and display the directory structure based on the options provided.
