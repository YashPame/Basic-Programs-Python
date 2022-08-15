
from math import sqrt, pow
# Python program for calculator

# Defining Function for various operators, n1,n2 be number variables
addition = lambda n1, n2: n1 + n2
subtraction = lambda n1, n2: n1 - n2
multiplication = lambda n1, n2: n1 * n2
division = lambda n1, n2: n1 / n2
remainder = lambda n1, n2: n1 % n2
power = lambda n1, n2: pow(n1,n2)
floor = lambda n1, n2: n1 // n2
sqRoot = lambda n: sqrt(n)
square = lambda n: pow(n, 2)
cube = lambda n: pow(n, 3)

# Defining Factorial Function
def Factorial(n):
    factorial = 1
    if n < 0:
        return 'Do not exist'
    elif n == 0:
        return 1
    else:
        for i in range(1, n + 1):
            factorial = factorial * i
        return factorial
def CheckPrime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print(n, "is Not Prime")
                break
        else:
            print(n, "is Prime")
    else:
        print(n, "is Not prime")


while True:
    # Taking Operator as Input
    print("Enter the operator\n"
          "+ for addition\n"
          "- for subtraction\n"
          "* for multiplication\n"
          "/ for division\n"
          "// for floor\n"
          "% for remainder\n"
          "! for factorial\n"
          "^2 for square\n"
          "|2 for sq root\n"
          "^3 for cube\n"
          "^ for x^y\n"
          "P to check Prime\n"
          "q to quit\n")
    op = input('Enter the operator: ')

    # If correct operator entered, take n1,n2 as inputs, using functions calculate
    if op == '+':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print(f"Addition, {n1} + {n2} = {addition(n1, n2)}")

    elif op == '-':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print(f"Subtraction, {n1} - {n2} = {subtraction(n1, n2)}")

    elif op == '*':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print(f"Multiplication, {n1} * {n2} = {multiplication(n1, n2)}")

    elif op == '/':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print(f"Division, {n1} / {n2} = {division(n1, n2)}")

    elif op == '%':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print(f"Remainder, {n1} % {n2} = {remainder(n1, n2)}")

    elif op == '//':
        n1 = float(input('Enter first number: '))
        n2 = float(input('Enter second number: '))
        print(f"floor, {n1} // {n2} = {floor(n1, n2)}")

    elif op == '^':
        n1 = float(input('Enter number: '))
        n2 = float(input('Enter power: '))
        print(f"Power, {n1}^{n2} = {power(n1, n2)}")

    elif op == '!':
        n = int(input('Enter number to find factorial of: '))
        print(f"Factorial, {n}! = {Factorial(n)}")

    elif op == '^2':
        n = float(input('Enter number: '))
        print(f"Square, {n}^2 = {square(n)}")

    elif op == '|2':
        n = float(input('Enter number: '))
        print(f"Square Root of {n} = {sqRoot(n)}")

    elif op == '^3':
        n = float(input('Enter number: '))
        print(f"Square, {n}^3 = {cube(n)}")

    elif op == 'P':
        n = int(input('Enter number to Check Prime: '))
        CheckPrime(n)

    elif op == 'q':
        exit()

    else:
        print('Invalid Operator Entered')
