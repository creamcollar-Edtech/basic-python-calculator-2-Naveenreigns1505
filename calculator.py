# calculator.py

def add(a, b):
    """Returns the sum of two numbers."""
    return a + b  # Correctly implemented logic

def subtract(a, b):
    """Returns the difference of two numbers."""
    return a - b  # Correctly implemented logic

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b  # Correctly implemented logic

def divide(a, b):
    """Returns the division of two numbers."""
    if b == 0:
        return "Error! Division by zero."  # Handle division by zero
    return a / b  # Correctly implemented logic

def main():
    print("Basic Python Calculator")
    operation = input("Enter operation (add, subtract, multiply, divide): ").strip().lower()

    if operation not in ['add', 'subtract', 'multiply', 'divide']:
        print("Invalid operation!")
        return

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if operation == 'add':
        result = add(a, b)
    elif operation == 'subtract':
        result = subtract(a, b)
    elif operation == 'multiply':
        result = multiply(a, b)
    elif operation == 'divide':
        result = divide(a, b)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()
