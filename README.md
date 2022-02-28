# python-module-starter

Starter template for Python module-based projects

## Development

Setup virtual environment

```bash
# macos/linux
python3 -m venv .venv
source .venv/bin/activate

# windows
python -m venv .venv
.venv\Scripts\activate
```

Update pip

```bash
python -m pip install --upgrade pip
```

Install requirements

```bash
pip install wheel

pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Run tests

Run all tests

```bash
python -m unittest
```

Run a specific test

```bash
python -m tests.test_module
```

### Pre-commit hook

Run on staged files

```bash
pre-commit run
```

Run on all files

```bash
pre-commit run --all-files
```
