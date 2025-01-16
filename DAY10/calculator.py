def cal():
    def add(n1, n2):
        return n1 + n2

    def divide(n1, n2):
        if n2 == 0:
            return "Error: Division by zero is not allowed."
        return n1 / n2

    def multiply(n1, n2):
        return n1 * n2

    def subtract(n1, n2):
        return n1 - n2

    def total(n1):
        """
        Performs calculations with the current value (n1) and allows the user
        to continue with the result or restart.
        """
        print("+\n-\n*\n/\n")
        operation = input("Pick an operation: ")

        n2 = float(input("Enter the second number: "))
        if operation == "+":
            result = add(n1, n2)
        elif operation == "-":
            result = subtract(n1, n2)
        elif operation == "*":
            result = multiply(n1, n2)
        elif operation == "/":
            result = divide(n1, n2)
        else:
            print("Invalid operation.")
            return total(n1)

        print(f"The result is: {result}")

        choice = input(f"Type 'y' to continue calculating with {result}, or 'n' to start over: ").lower()
        if choice == 'y':
            total(result)  # Continue with the current result
        elif choice == 'n':
            cal()  # Restart the calculator
        else:
            print("Invalid choice. Exiting.")

    # Start the calculation process
    n1 = float(input("Enter the first number: "))
    total(n1)


# Start the calculator
cal()
