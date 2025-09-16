from typing import Union, TypeVar

Number = TypeVar('Number', int, float)

def add(x: Number, y: Number) -> Number:
    """Return the sum of x and y."""
    return x + y

def subtract(x: Number, y: Number) -> Number:
    """Return the difference of x and y."""
    return x - y

def multiply(x: Number, y: Number) -> Number:
    """Return the product of x and y."""
    return x * y

def divide(x: Number, y: Number) -> Union[Number, str]:
    """Return x / y or an error message if y is zero."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def main() -> None:
    """Run an interactive command-line calculator."""
    print("Welcome to the Simple Calculator!")
    print("Operations: 1) Add  2) Subtract  3) Multiply  4) Divide")

    while True:
        choice = input("\nEnter operation (1-4) or 'q' to quit: ").lower()
        if choice == 'q':
            print("Thank you for using the calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select 1, 2, 3, or 4.")
            continue

        try:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        operations = {
            '1': (add, "Addition"),
            '2': (subtract, "Subtraction"),
            '3': (multiply, "Multiplication"),
            '4': (divide, "Division")
        }
        func, op_name = operations[choice]
        result = func(x, y)
        print(f"{op_name} result: {result}")

if __name__ == "__main__":
    main()
