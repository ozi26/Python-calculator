# Simple Python Calculator


This is a small demo Python project that provides basic calculator functions and a simple CLI.


## Files


- `calculator.py` — pure functions (add, subtract, multiply, divide) and a `main()` CLI guarded by `if __name__ == '__main__'`.
- `cli.py` — thin launcher you can run: `python cli.py`.
- `tests/` — pytest-based tests that validate calculator behavior.
- `.github/workflows/python-ci.yml` — GitHub Actions workflow that runs tests across multiple Python versions.


## Run locally


```bash
python -m venv .venv
source .venv/bin/activate # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
pytest
python cli.py
