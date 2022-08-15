import math

operator = input('Enter the operator (+,-,/,*,^,!): ')

if operator == '+':
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(f"{a} + {b} = {a + b}")

elif operator == '-':
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(f"{a} - {b} = {a - b}")

elif operator == '*':
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(f"{a} * {b} = {a * b}")

elif operator == '/':
    a = float(input('Enter first number: '))
    b = float(input('Enter second number: '))
    print(f"{a} / {b} = {a / b}")

elif operator == '^':
    a = float(input('Enter number: '))
    b = float(input('Enter power: '))
    print(f"{a}^{b} = {pow(a, b)}")

elif operator == '!':
    a = int(input('Enter number to find factorial of: '))
    print(f"{a}! = {math.factorial(a)}")

else:
    print('Invalid Operator')
