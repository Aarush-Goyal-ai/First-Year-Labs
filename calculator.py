def calculator():
    a = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    b = float(input("Enter second number: "))

    if op == '+':
        result = a + b
    elif op == '-':
        result = a - b
    elif op == '*':
        result = a * b
    elif op == '/':
        if b == 0:
            result = "Error: Division by zero"
        else:
            result = a / b
    else:
        result = "Error: Invalid operator"

    print("Result:", result)

calculator()
