def calculator():
    # Prompt the user for two numbers
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    # Display the operation choices
    print("\nChoose the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get the user's choice of operation
    operation = input("Enter the number corresponding to the operation: ")

    # Perform the calculation and display the result
    if operation == '1':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nError: Division by zero is not allowed.")
    else:
        print("\nInvalid operation choice.")

if __name__ == "__main__":
    calculator()
