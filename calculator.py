while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter operator (+, -, *, /, %, //, **): ")


        match operator:
            case "+":
                print("Result:", num1 + num2)

            case "-":
                print("Result:", num1 - num2)

            case "*":
                print("Result:", num1 * num2)

            case "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero")
                else:
                    print("Result:", num1 / num2)

            case "%":
                if num2 == 0:
                    print("Error: Cannot modulo by zero")
                else:
                    print("Result:", num1 % num2)

            case "//":
                if num2 == 0:
                    print("Error: Cannot divide by zero")
                else:
                    print("Result:", num1 // num2)

            case "**":
                print("Result:", num1 ** num2)

            case _:
                print("Error: Invalid operator!")
                print("Allowed operators: +, -, *, /, %, //, **")

    except ValueError:
        print("Error: Please enter valid numbers!")

    # Continue option
    choice = input("Do you want to continue? (yes/no): ").lower()

    if choice != "yes":
        print("Calculator closed. Thank you!")
        break