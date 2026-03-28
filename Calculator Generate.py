import random
import numbers

def generate_calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter 3rd number: "))
    # operaters = ['+','-','*','/']

    operaters = input("Enter operator (+, -, *, /): ")
    if operaters == '+':
        result = num1 + num2
    elif operaters == '-':
        result = num1 - num2
    elif operaters == '*':
        result = num1 * num2
    elif operaters == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"

    return f"{num1} {operaters} {num2} {operaters} {num3} = {result}"

calculator = generate_calculator()
print(calculator)