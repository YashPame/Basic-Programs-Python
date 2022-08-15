# Basic Questions
# Q. Write a Python program to find Factorial of number.

num = int(input("Enter a Number"))

factorial = 1

if num<0:
    print("Factorial do not exist")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range (1,num+1):
        factorial = factorial * i
    print(f"Factorial of {num} is {factorial}")