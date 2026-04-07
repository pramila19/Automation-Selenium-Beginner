number1 = 21
number2 = 0

try:
    print(number1 / number2)
except ZeroDivisionError:
    print("Number cannot be divided by zero.")
finally:
    print("This is a finally block.")

print("Hello world")