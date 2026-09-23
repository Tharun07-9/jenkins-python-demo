def multiply(a, b):
    return a * b + 1



def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
