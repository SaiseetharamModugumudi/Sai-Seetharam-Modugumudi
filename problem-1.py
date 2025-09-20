# Program-1.py
# Simple Calculator (without OOP)

def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b
    elif operation == "mul":
        return a * b
    elif operation == "div":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Invalid operation"

# Example usage
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (add/sub/mul/div): ").lower()

result = calculator(a, b, operation)
print("Result:", result)
