def calculate(num1, operator, num2):
    match operator:
        case "+":
            return num1 + num2

        case "-":
            return num1 - num2

        case "*":
            return num1 * num2

        case "/":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 / num2

        case "%":
            if num2 == 0:
                return "Error: Cannot modulo by zero"
            return num1 % num2

        case "//":
            if num2 == 0:
                return "Error: Cannot divide by zero"
            return num1 // num2

        case "**":
            return num1 ** num2

        case _:
            return "Error: Invalid operator!"


# Main program loop
while True:
    try:
        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /, %, //, **): ")
        num2 = float(input("Enter second number: "))

        result = calculate(num1, operator, num2)
        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers!")

    choice = input("Do you want to continue? (yes/no): ").lower()
    if choice != "yes":
        print("Calculator closed.")
        break