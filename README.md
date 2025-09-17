# Simple Calculator

A basic Python calculator application with a command-line interface for performing addition, subtraction, multiplication, and division.

## Features
- Supports basic arithmetic operations: add, subtract, multiply, divide.
- Handles division by zero with an error message.
- Interactive CLI for user input.
- Tested with `pytest` for reliability.

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the calculator:
   ```bash
   python calculator.py
   ```

## Testing
Run tests using `pytest`:
```bash
pytest -v
```

## GitHub Actions
The project uses GitHub Actions to run tests on push and pull requests to the `main` branch. The workflow:
- Tests on Python versions 3.8, 3.9, 3.10, and 3.11.
- Installs dependencies from `requirements.txt`.
- Runs tests with `pytest`.

## License
MIT
