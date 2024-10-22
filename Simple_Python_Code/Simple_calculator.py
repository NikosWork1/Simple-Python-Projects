def simple_calculator():
    try:
        # Ask the user to enter two numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Ask the user to choose an operation
        print("Select an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        operation = input("Enter the symbol of the operation you want to perform: ")

        # Perform the selected operation
        if operation == '+':
            result = num1 + num2
            print(f"The result of {num1} + {num2} is: {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"The result of {num1} - {num2} is: {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"The result of {num1} * {num2} is: {result}")
        elif operation == '/':
            # Handle division by zero error
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Invalid operation. Please enter one of +, -, *, or /.")

    except ValueError:
        # Handle invalid number input
        print("Error: Invalid input. Please enter numeric values.")


# Run the calculator
simple_calculator()
