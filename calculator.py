# calculator.py


def add(x: Number, y: Number) -> Number:
return x + y




def subtract(x: Number, y: Number) -> Number:
return x - y




def multiply(x: Number, y: Number) -> Number:
return x * y




def divide(x: Number, y: Number) -> Union[Number, str]:
"""Return x / y or a descriptive error string when dividing by zero.


You can change behavior to raise ZeroDivisionError if you prefer tests to expect exceptions.
"""
if y == 0:
return "Error! Division by zero."
return x / y




# Keep interactive CLI out of imports
def main() -> None:
# simple command-line interface — this runs only when executed as a script
print("Simple Calculator")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


while True:
choice = input("\nEnter choice (1/2/3/4) or 'q' to quit: ")


if choice == 'q':
print("Exiting calculator. Goodbye!")
break


if choice in ['1', '2', '3', '4']:
try:
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
except ValueError:
print("Invalid input! Please enter numbers only.")
continue


if choice == '1':
print(f"Result: {add(num1, num2)}")


elif choice == '2':
print(f"Result: {subtract(num1, num2)}")


elif choice == '3':
print(f"Result: {multiply(num1, num2)}")


elif choice == '4':
print(f"Result: {divide(num1, num2)}")
else:
print("Invalid choice. Please select a valid option.")




if __name__ == "__main__":
main()
