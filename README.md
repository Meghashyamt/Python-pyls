# Python-pyls

**pyproject.toml**

Create a pyproject.toml file in your project directory with the following content:

```bash
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"

[tool.pyls.scripts]
pyls = "script:main"
setup.py
```
Create a setup.py file in the same directory as pyproject.toml:

```bash
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
```
GitHub readme.md
Create a readme.md file in your project directory with the following content:


# Python Directory Listing (pyls)

This script provides a command-line tool (`pyls`) to print directory structures based on various options.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
Install the package:

```bash
pip install .
```
Usage
To print directory contents using pyls, run the following command:


pyls [OPTIONS]
Options
-A: Show all files
-l: Use a long listing format
-r: Reverse order
-t: Sort by time modified
-h: Display sizes in human readable format
--filter=TYPE: Filter by 'dir' or 'file'
--help: Display help and exit
Examples:


pyls -A            # Show all files
pyls -l            # Long listing format
pyls -t            # Sort by time modified
pyls --filter=dir  # Filter directories
pyls --help        # Display help
License
This project is licensed under the MIT License - see the LICENSE file for details.


Replace `yourusername` and `your-repository` with your GitHub username and repository name, respectively.

### GitHub Files

Make sure your project structure looks like this:

project/
│
├── pyproject.toml
├── setup.py
├── script.py
├── structure.json
├── README.md
└── LICENSE


- `pyproject.toml`: Contains build configuration.
- `setup.py`: Installs the package using setuptools.
- `script.py`: Your main script.
- `structure.json`: Example JSON file with directory structure.
- `README.md`: GitHub readme with installation and usage instructions.
- `LICENSE`: License file (e.g., MIT License).

### License

Include a LICENSE file (e.g., `LICENSE`) in your project directory with your preferred license (e.g., MIT License).


###Install the Project:

Now you can install your project using pip:

```bash
pip install .
```

Verify Installation:
After installation, you should be able to run the pyls command:

``bash
pyls
```
You should see the output:
LICENSE
README.md
ast
go.mod
lexer
main.go
parser
token




This setup will allow users to clone your repository, install your script as a packag
