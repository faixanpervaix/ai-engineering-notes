# Python Packages

## What Is a Python Package?

A Python package is a way to organize related Python code in folders.
It usually contains one or more Python modules (`.py` files) and often an `__init__.py` file.

- **Module**: a single Python file (for example, `math_utils.py`)
- **Package**: a folder that groups related modules (for example, `my_project/utils/`)

Packages help you:

- keep code organized,
- reuse code across projects,
- and share code with others.

## Types of Packages

### 1) Standard Library Packages (built into Python)

Examples: `math`, `os`, `json`, `datetime`

```python
import math

print(math.sqrt(25))
```

### 2) Third-Party Packages (installed from PyPI)

Examples: `numpy`, `pandas`, `requests`, `matplotlib`

Install them with `pip`:

```bash
python -m pip install numpy pandas requests
```

## Popular Package Examples

### 1) NumPy

NumPy is used for fast numerical computing and arrays.

```python
import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr.mean())
print(arr.sum())
```

Output:

```text
25.0
100
```

### 2) Pandas

Pandas is used for data analysis with tables (`DataFrame`).

```python
import pandas as pd

df = pd.DataFrame(
    {
        "name": ["Ava", "Zain", "Mina"],
        "score": [85, 92, 78],
    }
)

print(df)
print(df["score"].mean())
```

Output:

```text
   name  score
0   Ava     85
1  Zain     92
2  Mina     78
85.0
```

### 3) Requests

`requests` is used to send HTTP requests to APIs and websites.

```python
import requests

response = requests.get("https://api.github.com")
print(response.status_code)
```

Possible output:

```text
200
```

## How to Install These Packages

You can install `numpy`, `pandas`, and `requests` using either command:

```bash
python -m pip install numpy pandas requests
pip install numpy pandas requests
```

Both commands are valid.
Use `python -m pip` when you want to be sure packages are installed in the same Python interpreter you are running.
Use `pip` as a shorter command when your environment is already set correctly.

### Command Breakdown

For these commands:

```bash
python -m pip install numpy pandas requests
pip install numpy pandas requests
```

- `python`: runs the Python interpreter.
- `-m`: tells Python to run a module as a script.
- `pip`: the module being run (`pip` package manager).
- `install`: the pip action to install packages.
- `numpy pandas requests`: package names to install.

In `pip install ...`, `pip` directly runs the pip executable from your current environment.

Why use `python -m pip` instead of just `pip`?

- It ensures pip runs with the same Python interpreter/environment you selected.
- This helps avoid installing packages into the wrong Python version.

You can also install them one by one:

```bash
python -m pip install numpy
python -m pip install pandas
python -m pip install requests
```

To check if installation worked:

```bash
python -m pip show numpy pandas requests
```

## Other Useful `pip` Commands

### 1) List installed packages

```bash
python -m pip list
```

### 2) Check pip version

```bash
python -m pip --version
```

### 3) Upgrade a package

```bash
python -m pip install --upgrade numpy
```

### 4) Uninstall a package

```bash
python -m pip uninstall requests
```

### 5) Save current environment packages

```bash
python -m pip freeze > requirements.txt
```

### 6) Install from a `requirements.txt` file

```bash
python -m pip install -r requirements.txt
```

### 7) Check dependency issues

```bash
python -m pip check
```

## Quick Summary

- A package is a collection of related modules.
- Use built-in packages for common tasks.
- Install third-party packages with `pip`.
- Common beginner-friendly packages: `numpy`, `pandas`, and `requests`.


<hr/>

**Notebooks**

- [CSV Create and Read Using Panda](https://github.com/faixanpervaix/ai-engineering-notes/blob/main/notebooks/modle-1/class-3/02-csv-create-and-read.ipynb)

- [OpenStreetMap](https://github.com/faixanpervaix/ai-engineering-notes/blob/main/notebooks/modle-1/class-3/03-openstreetmap.ipynb)

- [QRCode Generator](https://github.com/faixanpervaix/ai-engineering-notes/blob/main/notebooks/modle-1/class-3/04-qrcode-generator.ipynb)

- [Audio Transcribing](https://github.com/faixanpervaix/ai-engineering-notes/blob/main/notebooks/modle-1/class-3/01-audi-transcribing.ipynb)