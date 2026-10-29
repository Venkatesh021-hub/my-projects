"""Day 1 · Step 0 — a normal Python program. It works, but only for the person sitting at this keyboard.
Run:  python 01_calculator_script.py      (from Interns/basic/3_Calculator.py)"""
# Define the function to perform arithmetic operations
def calculate(num1, num2, operation):
    if operation == "sum":
        return num1 + num2
    elif operation == "sub":
        return num1 - num2
    elif operation == "mul":
        return num1 * num2
    elif operation == "div":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is undefined."
    else:
        return "Error: Unsupported operation."

# Get user input
print("Calculator")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (sum, sub, mul, div): ")

# Call the function
result = calculate(num1, num2, operation)

print("Result:", result)
